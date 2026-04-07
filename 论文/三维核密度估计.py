import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import PolyCollection  # 新增：专门用于在3D坐标系中绘制稳定的填充多边形

# ==========================================
# 0. 全局设置：字体与样式
# ==========================================
# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei', 'Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False

# 1. 读取数据并初始化 3D 画布
df = pd.read_csv('Data_score_Final.csv')
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

years = sorted(df['年份'].unique())
colors = plt.cm.viridis(np.linspace(0.2, 0.9, len(years)))

# 2. 循环计算并绘制每年的三维核密度图
for i, year in enumerate(years):
    y_data = df[df['年份'] == year]['Y(VIKOR得分)'].values
    n = len(y_data)

    # Silverman 法则计算带宽，并生成评估网格
    bw = 1.06 * np.std(y_data) * (n ** (-0.2))
    x_eval = np.linspace(0, 1, 100)

    # 纯 Numpy 矩阵化计算高斯核密度 (替代 scipy)
    diff = x_eval[None, :] - y_data[:, None]
    z_eval = np.sum(np.exp(-0.5 * (diff / bw) ** 2) / (bw * np.sqrt(2 * np.pi)), axis=0) / n

    # 绘制 3D 曲线
    ax.plot(x_eval, z_eval, zs=year, zdir='y', linewidth=2, color=colors[i], label=f'{year}年')

    # 绘制带透明度的 3D 填充多边形
    verts = [(x_eval[0], 0)] + list(zip(x_eval, z_eval)) + [(x_eval[-1], 0)]
    poly = PolyCollection([verts], facecolors=colors[i], alpha=0.4)
    ax.add_collection3d(poly, zs=year, zdir='y')

# 3. 设置坐标轴、标题与视角
ax.set(xlabel='\n综合配置得分 (VIKOR)', ylabel='\n年份', zlabel='\n核密度 (Density)',
       title='2020-2024年中国省级紧急医疗配置三维核密度演进')
ax.set_yticks(years)
ax.view_init(elev=25, azim=-50)

# 显示图例并优化布局
plt.legend(loc='upper left', bbox_to_anchor=(1.05, 1))
plt.tight_layout()

# 保存或展示图表
plt.savefig('图5_3DKDE演进图.png', dpi=300, bbox_inches='tight')
plt.show()
    # ========================基于 GTWR 的时空异质性测算与可视化=================================



# 1. 基础设置与数据读取
plt.rcParams['font.sans-serif'] = ['SimHei']  # 正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 正常显示负号

df = pd.read_csv("Data_score_Final.csv")

# 2. 特征标准化与时空坐标提取
X = df[['X1(老龄化)', 'X2(人口密度)', 'X3(GDP)', 'X4(财政占比)']].values
X_std = (X - X.mean(axis=0)) / X.std(axis=0)
X_mat = np.c_[np.ones(X_std.shape[0]), X_std] # 增广矩阵加截距
Y_vec = df['Y(VIKOR得分)'].values

# 直接提取源数据经纬度与年份并标准化
ST = df[['经度', '纬度', '年份']].values
ST_std = (ST - ST.mean(axis=0)) / ST.std(axis=0)

# 3. 白盒化 GTWR 矩阵解算 (极致精简版)
n = len(df)
beta_gtwr = np.zeros((n, X_mat.shape[1]))

# 广播机制计算全样本距离矩阵
diff = ST_std[:, np.newaxis, :] - ST_std[np.newaxis, :, :]
distances = np.sqrt(np.sum(diff**2, axis=-1))
h = np.median(distances) / 2 # 设定经验带宽

for i in range(n):
    # 高斯核函数计算空间权重 W_i
    W_i = np.diag(np.exp(-0.5 * (distances[i] / h)**2))
    XT_Wi = X_mat.T @ W_i
    try:
        # 正规方程极速求解
        beta_gtwr[i] = np.linalg.inv(XT_Wi @ X_mat) @ XT_Wi @ Y_vec
    except np.linalg.LinAlgError:
        pass # 规避奇异矩阵报错

df['Beta_2(人口密度)'] = beta_gtwr[:, 2]
df['Beta_4(财政占比)'] = beta_gtwr[:, 4]

# 4. 可视化与图片本地保存
target_provs = ['上海市', '北京市', '浙江省', '四川省', '甘肃省', '贵州省']
# 提取 2024 年数据并按财政拉动效应降序排列
df_2024 = df[(df['年份'] == 2024) & (df['省份'].isin(target_provs))].sort_values('Beta_4(财政占比)', ascending=False)

fig, ax = plt.subplots(figsize=(10, 6))
x = np.arange(len(df_2024))
w = 0.35

# 绘制双向对比柱状图
rects1 = ax.bar(x - w/2, df_2024['Beta_4(财政占比)'], w, label='财政拉动边际效应 (正向)', color='indianred')
rects2 = ax.bar(x + w/2, df_2024['Beta_2(人口密度)'], w, label='人口挤兑边际效应 (负向)', color='steelblue')

ax.set_ylabel('GTWR 偏回归系数大小', fontsize=12)
ax.set_title('2024年典型东中西部省份驱动机制异质性对比 (GTWR)', fontsize=15, pad=15)
ax.set_xticks(x)
ax.set_xticklabels(df_2024['省份'], fontsize=11)
ax.axhline(0, color='black', linewidth=1)
ax.legend()

# 循环为两组柱状图添加数值标签 (严格保留三位小数)
for rects in [rects1, rects2]:
    for rect in rects:
        h_val = rect.get_height()
        va, offset = ('bottom', 3) if h_val > 0 else ('top', -12)
        ax.annotate(f'{h_val:.3f}', xy=(rect.get_x() + rect.get_width() / 2, h_val),
                    xytext=(0, offset), textcoords="offset points", ha='center', va=va)

plt.tight_layout()


save_name = "图6_2024年典型东中西部省份驱动机制异质性对比.png"
plt.savefig(save_name, dpi=300, bbox_inches='tight')
print(f"✅ 图表已成功生成并保存为：{save_name}")

