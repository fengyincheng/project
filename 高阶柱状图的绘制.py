from pyecharts.charts import Bar,Timeline
from pyecharts.options import LabelOpts

bar_1 = Bar()
bar_1.add_xaxis(['中国','美国','英国'])
bar_1.add_yaxis("GPT",[50,30,90],label_opts=LabelOpts(position="right"))
bar_1.reversal_axis()
bar_1.render("基础柱状图的绘制.html")

bar_2 = Bar()
bar_2.add_xaxis(['中国','美国','英国'])
bar_2.add_yaxis("GPT",[200,100,60],label_opts=LabelOpts(position="right"))
bar_2.reversal_axis()
bar_2.render("基础柱状图的绘制.html")

bar_3 = Bar()
bar_3.add_xaxis(['中国','美国','英国'])
bar_3.add_yaxis("GPT",[900,300,600],label_opts=LabelOpts(position="right"))
bar_3.reversal_axis()


timeline = Timeline()
timeline.add(bar_1,"2010")
timeline.add(bar_2,"2011")
timeline.add(bar_3,"2012")
#绘图使用时间线绘图，不是在用bar了
#自动播放
timeline.add_schema(
    play_interval=1000, #时间间隔，单位毫秒
    is_timeline_show=True,
    is_auto_play=True,
    is_loop_play=True,
)
timeline.render("高阶柱状图的绘制.html")

