from pyecharts.charts import Bar
from pyecharts.options import LabelOpts
bar = Bar()
bar.add_xaxis(['中国','美国','英国'])
bar.add_yaxis("GPT",[50,30,90],label_opts=LabelOpts(position="right"))
bar.reversal_axis()
bar.render("基础柱状图的绘制.html")
