
import json
#数据处理
with open("E:\美国.txt","r",encoding="utf-8") as f:
    us_new_data = json.load(f)
    #美国这边少了几行是因为我已经把数据不规范的内容删掉了


with open("E:\日本.txt","r",encoding="utf-8") as g:
    old_text_jp = g.read()
    
    new_text_jp = old_text_jp.replace("jsonp_1629350871167_29498(","") #query删除多余部分
    new_text_jp = new_text_jp[: -2]    #去掉结尾的');'
with open("E:\印度.txt","r+",encoding="utf-8") as z:
    old_text_id = z.read()
    
    new_text_id = old_text_id.replace("jsonp_1629350745930_63180("," ") #query删除多余部分
    new_text_id= new_text_id[ : -2]    #去掉结尾的');'

jp_dict = json.loads(new_text_jp)  #load是导入文本文件file去转格式，而loads是导入文本文件的内容这里是str去转格式，因为我用代码对日本和印度的文本进行处理，所以原本的文本文件被我的一通操作搞成了str，故这里用loads而非load
id_dict = json.loads(new_text_id)



#数据的获取，为x,y轴的数据做准备
us_y_data = us_new_data['data'][0]['trend']['list'][0]['data'][ :314]  #累计确诊人数？
us_x_data = us_new_data['data'][0]['trend']['updateDate'][ :314]  #2020年日期
jp_y_data = jp_dict['data'][0]['trend']['list'][0]['data'][ :315]  #累计确诊人数？
jp_x_data = jp_dict['data'][0]['trend']['updateDate'][ :315]  #2020年日期
id_y_data = id_dict['data'][0]['trend']['list'][0]['data'][ :314]  #累计确诊人数？
id_x_data = id_dict['data'][0]['trend']['updateDate'][ :314]  #2020年日期

#模块的导入
from pyecharts.charts import Line
from pyecharts.options import TitleOpts,LegendOpts,ToolboxOpts,VisualMapOpts,LabelOpts
line = Line() 
line.add_xaxis(us_x_data)  #x轴是公用的
line.add_yaxis("美国的确诊人数",us_y_data,label_opts=LabelOpts(is_show=False))
line.add_yaxis("日本的确诊人数",jp_y_data,label_opts=LabelOpts(is_show=False))  #隐藏折线图直接显示数据
line.add_yaxis("印度的确诊人数",id_y_data,label_opts=LabelOpts(is_show=False))

line.set_global_opts(
    title_opts=TitleOpts(title="2020美日印疫情确诊人数图",pos_top="5%",pos_left="center"),
    legend_opts=LegendOpts(is_show = True),
    toolbox_opts=ToolboxOpts(is_show = True),
    # visualmap_opts=VisualMapOpts(is_show = True)
    )

line.render()

