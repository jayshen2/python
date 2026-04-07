import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# =========================================================
# 0. 全局设置与数据读取
# =========================================================
# 设置中文字体，防止图表中的中文和负号变成方块（兼容Win和Mac）
plt.rcParams['font.sans-serif'] = ['SimHei', 'Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False

df = pd.read_csv('Data.csv')

# 定义需要计算的7个核心指标及其方向（1代表越大越好，-1代表越小越好）
indicators = ['每千人口执业（助理）医师数', '急诊科医护人员占比', '每万人口救护车保有量',
              '三甲医院急诊床位数', '地方财政医疗卫生支出占比', '人均GDP', '人均医疗负担']
polarities = [1, 1, 1, 1, 1, 1, -1]

# 提取这7列的数据形成矩阵 X
X = df[indicators].values
n, m = X.shape  # n是样本总数，m是指标总数(7)

# =========================================================
# 1. 数据极差标准化处理 (消除量纲差异)
# =========================================================
X_norm = np.zeros_like(X, dtype=float)
for j in range(m):
    col_data = X[:, j]
    if polarities[j] == 1:
        # 正向指标：(当前值 - 最小值) / (最大值 - 最小值)
        X_norm[:, j] = (col_data - np.min(col_data)) / (np.max(col_data) - np.min(col_data) + 1e-9)
    else:
        # 负向指标（如人均医疗负担）：(最大值 - 当前值) / (最大值 - 最小值)
        X_norm[:, j] = (np.max(col_data) - col_data) / (np.max(col_data) - np.min(col_data) + 1e-9)

# =========================================================
# 2. 熵权法计算 (测度数据的客观信息量大小)
# =========================================================
# 计算特征比重 P
P = X_norm / (np.sum(X_norm, axis=0) + 1e-9)
# 计算信息熵 Entropy (-1/ln(n) * sum(P * lnP))
entropy = -1.0 / np.log(n) * np.sum(P * np.where(P == 0, 0, np.log(P + 1e-9)), axis=0)
# 计算熵权法权重 w1
w_entropy = (1 - entropy) / np.sum(1 - entropy)

# =========================================================
# 3. CRITIC法计算 (测度指标的波动性与冲突性)
# =========================================================
# 计算各指标的标准差（波动性）
std_dev = np.std(X_norm, axis=0)
# 计算指标间的相关系数矩阵
corr_matrix = np.corrcoef(X_norm.T)
# 计算冲突性 (1 - 相关系数 的和)
conflict = np.sum(1 - corr_matrix, axis=1)
# 计算 CRITIC 权重 w2 (波动性 * 冲突性 归一化)
w_critic = (std_dev * conflict) / np.sum(std_dev * conflict)

# =========================================================
# 4. 博弈论组合赋权 (寻找纳什均衡的最优权重)
# =========================================================
# 构建博弈论矩阵的 A 和 B，求解线性方程组 A * alpha = B
A_mat = np.array([[np.dot(w_entropy, w_entropy), np.dot(w_entropy, w_critic)],
                  [np.dot(w_entropy, w_critic), np.dot(w_critic, w_critic)]])
B_vec = np.array([np.dot(w_entropy, w_entropy), np.dot(w_critic, w_critic)])

# 求解得出组合系数 alpha1 和 alpha2
coeffs = np.linalg.solve(A_mat, B_vec)
coeffs_norm = np.abs(coeffs) / np.sum(np.abs(coeffs))

# 最终博弈论权重 w_final = alpha1 * w1 + alpha2 * w2
w_final = coeffs_norm[0] * w_entropy + coeffs_norm[1] * w_critic

# =========================================================
# 5. VIKOR 多准则妥协评价 (计算最终得分)
# =========================================================
v = 0.5  # 决策机制系数，0.5代表群体效用与个别遗憾同等重要

# 计算群体效用值 S 和 个别遗憾值 R
S = np.array([np.sum(w_final * (1 - X_norm[i, :])) for i in range(n)])
R = np.array([np.max(w_final * (1 - X_norm[i, :])) for i in range(n)])

# 计算妥协指数 Q
Q = v * (S - np.min(S)) / (np.max(S) - np.min(S) + 1e-9) + (1 - v) * (R - np.min(R)) / (np.max(R) - np.min(R) + 1e-9)

# 转换成正向得分：得分越高配置越好
df['Y(VIKOR得分)'] = 1 - Q

# =========================================================
# 6. 生成并导出两个 CSV 数据文件
# =========================================================
# 重命名列以匹配论文要求
df = df.rename(columns={
    '省份名称': '省份', '所属区域标签': '所属大区',
    '老龄化率': 'X1(老龄化)', '人口密度': 'X2(人口密度)',
    '人均GDP': 'X3(GDP)', '地方财政医疗卫生支出占比': 'X4(财政占比)'
})

# 【数据1】：导出 31省微观面板数据 (供后续算Dagum和回归用)
output_cols = ['省份', '年份', '所属大区', '经度', '纬度', 'Y(VIKOR得分)', 'X1(老龄化)', 'X2(人口密度)', 'X3(GDP)',
               'X4(财政占比)']
base_df = df[[col for col in output_cols if col in df.columns]]
base_df.to_csv('Data_score_Final.csv', index=False, encoding='utf-8-sig')
print(">>> 已生成数据1: Data_score_Final.csv")

# 【数据2】：导出 7大区域聚合均值数据 (供画图用)
regional_avg = base_df.groupby(['年份', '所属大区']).mean(numeric_only=True).reset_index()
regional_avg.to_csv('Regional_Average_Score.csv', index=False, encoding='utf-8-sig')
print(">>> 已生成数据2: Regional_Average_Score.csv")

# =========================================================
# 7. 绘制图表 (图2折线图 和 图3雷达图)
# =========================================================
print(">>> 正在生成图表...")

# 【绘图1】：图2 七大区域演变折线图
plt.figure(figsize=(10, 6))
regions = regional_avg['所属大区'].unique()
markers = ['o', 's', '^', 'D', 'v', '<', '>']

# 循环画出7条大区的折线
for i, region in enumerate(regions):
    region_data = regional_avg[regional_avg['所属大区'] == region]
    plt.plot(region_data['年份'], region_data['Y(VIKOR得分)'],
             marker=markers[i], markersize=8, linewidth=2, label=region)

plt.title('2020-2024年中国七大区域紧急医疗配置得分演变', fontsize=16, pad=15)
plt.xticks(sorted(regional_avg['年份'].unique()))
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.savefig('图2_七大区域演变折线图.png', dpi=300)

# 【绘图2】：图3 2024年典型大区对比雷达图
df_2024 = regional_avg[regional_avg['年份'] == 2024].copy()

# 选择要在雷达图上显示的5个指标
radar_cols = ['X1(老龄化)', 'X2(人口密度)', 'X3(GDP)', 'X4(财政占比)', 'Y(VIKOR得分)']
radar_data = df_2024.groupby('所属大区')[radar_cols].mean()

# 对雷达图数据做0-1标准化，确保形状能放在同一个多边形里对比
radar_norm = (radar_data - radar_data.min()) / (radar_data.max() - radar_data.min() + 1e-9)

N = len(radar_cols)
angles = [n / float(N) * 2 * np.pi for n in range(N)]
angles += angles[:1]  # 闭合圆环

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# 挑选论文中用于分析的三个代表性区域
target_regions = ['西南地区', '华东地区', '华北地区']
colors = ['#d62728', '#1f77b4', '#2ca02c']

for i, region in enumerate(target_regions):
    if region in radar_norm.index:
        values = radar_norm.loc[region].values.flatten().tolist()
        values += values[:1]
        ax.plot(angles, values, linewidth=2, linestyle='solid', label=region, color=colors[i])
        ax.fill(angles, values, color=colors[i], alpha=0.15)

# 设置雷达图顶点标签名称（去除变量名的括号后缀，保持图面整洁）
clean_labels = [col.split('(')[-1].replace(')', '') if '(' in col else col for col in radar_cols]
plt.xticks(angles[:-1], clean_labels, size=12)
ax.set_yticklabels([])  # 隐藏极坐标的数字圈
plt.title('2024年典型大区医疗资源配置结构雷达图', size=16, pad=20)
plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))

plt.tight_layout()
plt.savefig('图3_大区对比雷达图.png', dpi=300)
print(">>> 全部处理完成！已成功生成 2 个数据文件 和 2 张图表。")