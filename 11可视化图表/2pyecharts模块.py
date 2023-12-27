from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LegendOpts, ToolboxOpts, VisualMapOpts
# 创建一个折线图对 象
Line = Line()
Line.add_xaxis(["中国", "美国", "英国"])
Line.add_yaxis("GDP", [20, 30, 20])
# 设置全局配置项
Line.set_global_opts(
    title_opts=TitleOpts(title="GDP展示", pos_left="center", pos_bottom="1%"),
    # 设置标题名称为GDP展示，标题居中，距离底部百分之1
    legend_opts=LegendOpts(is_show=True),
    # 图例展示
    toolbox_opts=ToolboxOpts(is_show=True),
    # 工具栏展示
    visualmap_opts=VisualMapOpts(is_show=True)
    # 视觉映射展示
    # 更多的全局配置项可以使用pyechart全局配置项可以从官网上找
)
Line.render()
# 线条渲染