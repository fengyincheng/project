from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts
map = Map()
data = [
    ("北京市",99),
    ("上海市",130),
    ("新疆维吾尔自治区",9),
    ("湖南省",300),
    ("江西省",150)
    ]
map.add("测试地图",data,"china")
map.set_global_opts(
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min": 1, "max": 9, "label": "1-9", "color": "#EB9E41"},
            {"min": 10, "max": 99, "label": "10-99", "color": "#12ACC7"},  #加逗号，真是愁死我了，说什么未关闭应该就是逗号的锅
            {"min": 100, "max": 500, "label": "100-500", "color": "#A30B3E"},
        ]
    )
)
map.render()
