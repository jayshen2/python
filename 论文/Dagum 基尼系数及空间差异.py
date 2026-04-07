import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def calculate_dagum_gini(file_name='Data_score_Final.csv'):
    # ==========================================
    # 1. 环境准备与数据加载
    # ==========================================
    try:
        df = pd.read_csv(file_name)
    except:
        return  # 静默退出，不输出错误数据

    # 设置绘图字体（黑体），解决中文乱码
    plt.rcParams.update({'font.sans-serif': ['SimHei'], 'axes.unicode_minus': False})

    years = sorted(df['年份'].unique())
    results = []

    # ==========================================
    # 2. 核心数学计算逻辑 (Dagum 分解)
    # ==========================================
    for year in years:
        df_y = df[df['年份'] == year]
        val, grp = df_y['Y(VIKOR得分)'].values, df_y['所属大区'].values
        n, mean_all = len(val), np.mean(val)

        # 计算总体基尼系数 G：衡量全样本的绝对差异
        # 利用 [:, None] 广播机制生成差值矩阵，等同于双重求和公式
        G = np.sum(np.abs(val[:, None] - val[None, :])) / (2 * n ** 2 * mean_all)

        # 预计算各子区域指标：均值(m)、样本占比(p)、份额占比(s)
        g_info = {g: {'v': val[grp == g], 'n': sum(grp == g), 'm': np.mean(val[grp == g]),
                      'p': sum(grp == g) / n, 's': (sum(grp == g) * np.mean(val[grp == g])) / (n * mean_all)}
                  for g in np.unique(grp)}

        Gw, Gnb, Gt = 0.0, 0.0, 0.0
        g_list = list(g_info.keys())

        # 计算区域内差异贡献 Gw (Within-group)
        for g in g_list:
            v, ni, mi, pi, si = g_info[g]['v'], g_info[g]['n'], g_info[g]['m'], g_info[g]['p'], g_info[g]['s']
            gi = np.sum(np.abs(v[:, None] - v[None, :])) / (2 * ni ** 2 * mi)  # 区域内基尼系数
            Gw += gi * pi * si

        # 计算区域间净差异 Gnb 与超变密度 Gt (基于组间分布重叠程度)
        for i in range(len(g_list)):
            for k in range(i + 1, len(g_list)):
                g1, g2 = g_list[i], g_list[k]
                # 排序：j为高均值组，h为低均值组，符合学术定义约束
                j, h = (g1, g2) if g_info[g1]['m'] > g_info[g2]['m'] else (g2, g1)
                vj, vh, mj, mh = g_info[j]['v'], g_info[h]['v'], g_info[j]['m'], g_info[h]['m']

                # gjh 为跨组基尼系数，反映两组间的平均差异
                gjh = np.sum(np.abs(vj[:, None] - vh[None, :])) / (len(vj) * len(vh) * (mj + mh))

                # 计算 Djh：相对影响系数，用于剥离“均值差”和“分布重叠”
                diff = vj[:, None] - vh[None, :]
                djh = np.sum(diff[diff > 0]) / (len(vj) * len(vh))  # 组间净差值
                pjh = np.sum(-diff[diff < 0]) / (len(vj) * len(vh))  # 组间交叉项/重叠值
                Djh = (djh - pjh) / (djh + pjh)  # 相对位移值

                # 权重项计算
                weight = (g_info[j]['p'] * g_info[h]['s'] + g_info[h]['p'] * g_info[j]['s'])
                Gnb += gjh * weight * Djh  # 区域间纯净差异贡献
                Gt += gjh * weight * (1 - Djh)  # 样本分布重叠导致的差异（交叉效应）

        # 汇总各年份贡献率数据
        results.append({'年份': year, 'Gw_rate': Gw / G * 100, 'Gnb_rate': Gnb / G * 100, 'Gt_rate': Gt / G * 100})

    # ==========================================
    # 3. 绘图输出逻辑 (不输出文本数据)
    # ==========================================
    df_res = pd.DataFrame(results)

    # 创建画布，设置长宽比
    plt.figure(figsize=(10, 6))

    # 绘制堆叠面积图：直观展示三部分贡献率随时间的变化演进
    # 颜色选取：#4E79A7(深蓝-区域内), #F28E2B(橙色-区域间), #E15759(红色-超变)
    plt.stackplot(df_res['年份'], df_res['Gw_rate'], df_res['Gnb_rate'], df_res['Gt_rate'],
                  labels=['区域内贡献 (Gw)', '区域间净贡献 (Gnb)', '超变密度贡献 (Gt)'],
                  colors=['#4E79A7', '#F28E2B', '#E15759'], alpha=0.85, edgecolor='white', linewidth=0.5)

    # 完善图表学术格式
    plt.title('2020-2024年中国省级紧急医疗配置空间差异溯源 (Dagum基尼分解)', fontsize=14, pad=20)
    plt.xlabel('年份', fontsize=12)
    plt.ylabel('方差贡献率 (%)', fontsize=12)
    plt.xticks(years)  # 强制显示所有年份刻度
    plt.ylim(0, 100)  # 贡献率上限固定为100%

    # 图例设置：水平排列并置于图表下方，避免遮挡曲线
    plt.legend(loc='lower center', bbox_to_anchor=(0.5, -0.2), ncol=3, frameon=False, fontsize=10)

    # 优化布局并保存图表
    plt.tight_layout()
    plt.savefig('图4_Dagum.png', dpi=300)
    # 不调用 plt.show() 以保持输出简洁


if __name__ == "__main__":
    calculate_dagum_gini()