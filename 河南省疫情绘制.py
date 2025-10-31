import json
with open("E:\疫情.txt","r",encoding="utf-8") as file:
    data_all = json.load(file)
    hn_data = data_all['areaTree'][0]['children'][3]['children']
    data_list=[]
    for cities_data in hn_data: 
        if cities_data["name"] not in ['济源市']:  
            cities_data_name = cities_data["name"] + "市"
            cities_data_confirm = cities_data['total']['confirm']
        else:    
            cities_data_name = cities_data["name"]
            cities_data_confirm = cities_data['total']['confirm']
        data_list.append((cities_data_name,cities_data_confirm))
print(data_list)


from pyecharts.charts import Map
map = Map()
map.add("河南疫情图", data_list, "河南")

from pyecharts.options import TitleOpts,VisualMapOpts
map.set_global_opts(
    title_opts=TitleOpts(title="河南省疫情图",pos_bottom="1%",pos_left="center"),#逗号！！！！
    visualmap_opts=VisualMapOpts(is_show=True,is_piecewise=True,#逗号！！！！！
                                 pieces=[
                                     {"min": 0, "max": 9,"label":"0-9","color":"#FF7181"},
                                     {"min": 10, "max": 99, "label": "10-99", "color": "#FFF666"},
                                     {"min": 99, "max": 499, "label": "99-499", "color": "#85DE3C"},  #woc,这个死东西，min和max都要加"",冒号后面要空格，逗号后面居然也该死的要空格，快把我整死了，对了，每一个字典末尾也要逗号，包括最后一个
                                     {"min": 499, "max": 999, "label": "499-999", "color": "#3DABDE"},
                                     {"min": 1000, "max": 9999, "label": "1000-9999", "color": "#ED590F"},
                                     {"min": 10000, "label": "10000+", "color": "#F50202"},
                                 ]
                                 )
    
)
map.render()

        
    

