# import json
# data = {"name:":"黄舒宇","age":18}
# x = json.dumps(data,ensure_ascii=False)
# print(f"转换成json后的文件是：{x}")

# s= '{"name:": "\u9ec4\u8212\u5b87", "age":18}'
# y = json.loads(s)
# print(type(y))
# print(y)


from pyecharts.charts import Line
line = Line()
#X轴数据
line.add_xaxis(["中国","美国","英国"])
#Y轴数据
line.add_yaxis("GDP",[300,50,20])
#通过render方法生成图表
line.render()
