import pandas as pd

# 读取数据
df = pd.read_csv('Data_score_Final.csv')

# 1. 全局极差标准化计算，求出 X1 和 X2 的全局最值
x1_min, x1_max = df['X1(老龄化)'].min(), df['X1(老龄化)'].max()
x2_min, x2_max = df['X2(人口密度)'].min(), df['X2(人口密度)'].max()

# 应用标准化公式
df['X1_norm'] = (df['X1(老龄化)'] - x1_min) / (x1_max - x1_min)
df['X2_norm'] = (df['X2(人口密度)'] - x2_min) / (x2_max - x2_min)

# 2. 计算时空急救综合压力指数 (SEMSI)
df['SEMSI'] = (0.5 * df['X1_norm'] + 0.5 * df['X2_norm']) / df['Y(VIKOR得分)']

# 3. 循环计算目标省份的各项指标
target_provinces = ['上海市', '甘肃省', '四川省']
results = []

for prov in target_provinces:
    prov_data = df[df['省份'] == prov]

    # 提取首尾年份的压力指数
    semsi_2020 = prov_data[prov_data['年份'] == 2020]['SEMSI'].values[0]
    semsi_2024 = prov_data[prov_data['年份'] == 2024]['SEMSI'].values[0]

    # 提取首尾年份的供给得分，并计算绝对增加量 (Delta Y)
    y_2020 = prov_data[prov_data['年份'] == 2020]['Y(VIKOR得分)'].values[0]
    y_2024 = prov_data[prov_data['年份'] == 2024]['Y(VIKOR得分)'].values[0]
    delta_y = y_2024 - y_2020

    # 计算五年期间财政医疗支出占比的平均值 (X4_avg)
    x4_avg = prov_data['X4(财政占比)'].mean()

    # 计算财政时空配置拉动指数 (FALI)
    fali = (delta_y / x4_avg) * 100

    # 汇总结果，严格保留三位小数输出
    results.append({
        '地区': prov,
        '2020年压力': round(semsi_2020, 3),
        '2024年压力': round(semsi_2024, 3),
        '五年平均财政占比(%)': round(x4_avg, 3),
        '供给增加量': round(delta_y, 3),
        '财政拉动指数(FALI)': round(fali, 3)
    })

# 4. 生成并输出最终结果表
result_df = pd.DataFrame(results)
print(result_df)