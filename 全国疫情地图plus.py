import json
with open("E:\疫情.txt","r",encoding="utf_8") as flie:
    zh_data = json.load(flie)
    province_data_list = zh_data['areaTree'][0]['children']
    data_list = []
    #遍历列表取到省份名称和确诊人数，让省份和确诊人数组装成元组封装到列表中
    for province_data in province_data_list:
        province_name = province_data['name']
        province_confirm = province_data['total']['confirm']
        data_list.append((province_name,province_confirm))
from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts
map = Map()
map.add("全国疫情图",data_list,"china")
map.set_global_opts(
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
                {"min": 1, "max": 9, "label": "0-9", "color":  "#5499D0"},
                {"min": 10, "max": 99, "label": "10-99", "color": "#FFF666"},
                {"min": 99, "max": 499, "label": "99-499", "color": "#C36B13"},  #woc,这个死东西，min和max都要加"",冒号后面要空格，逗号后面居然也该死的要空格，快把我整死了，对了，每一个字典末尾也要逗号，包括最后一个
                {"min": 499, "max": 999, "label": "499-999", "color": "#D44A00"},
                {"min": 1000, "max": 9999, "label": "1000-9999", "color": "#80210B"},
                {"min": 10000, "label": "10000+", "color": "#F50202"},
        ]
    )
)

map.render()