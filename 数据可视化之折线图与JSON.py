# import json
# data = {"name:":"黄舒宇","age":18}
# x = json.dumps(data,ensure_ascii=False)
# print(f"转换成json后的文件是：{x}")

# s= '{"name:": "\u9ec4\u8212\u5b87", "age":18}'
# y = json.loads(s)
# print(type(y))
# print(y)


from pyecharts.charts import Line
from pyecharts.options import TitleOpts,LegendOpts,ToolboxOpts,VisualMapOpts
line = Line()
#X轴数据
line.add_xaxis(["中国","美国","英国"])
#Y轴数据
line.add_yaxis("GDP",[300,50,20])
#通过render方法生成图表

#增加全局配置项
line.set_global_opts(
    title_opts=TitleOpts(title = "GTP对比图",pos_left="center",pos_bottom="1%"),#标题
    legend_opts=LegendOpts(is_show=True),#图例
    toolbox_opts=ToolboxOpts(is_show=True),#工具栏
    visualmap_opts=VisualMapOpts(is_show=True))#视觉映射






line.render()
