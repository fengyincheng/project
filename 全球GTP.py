with open(r"E:\1960-2019全球GDP数据.csv","r",encoding="GB2312") as f:
    data_line = f.readlines() #readlines读成列表
    data_line.pop(0)  #这列表是每行为一个元素，想验证很简单，print一下看看逗号分隔的地方就行了
    clean_data = []
    for new_data in data_line:
        new_data = new_data.replace("\n","")
        clean_data.append(new_data)
        
    #创建字典{1999:{中国：gdp}}
    data_dict = {}
for line in clean_data:
    parts = line.split(",")
    if len(parts) < 3:
        continue  # 跳过格式异常的数据行
    try:
        year = int(parts[0])
        country = parts[1]
        gdp = float(parts[2])
    except (ValueError, IndexError):
        continue  # 跳过无法解析的数据行
    if year not in data_dict or not isinstance(data_dict.get(year), list):
        data_dict[year] = []
    data_dict[year].append([country, gdp])

#对年份排序，使用sorted()
# 提示：sorted() 可以对字典的keys排序
sorted_years = sorted(data_dict.keys())  # 得到排序后的年份列表

# 然后创建新字典
sorted_dict = {}
for year in sorted_years:
    # 对每个年份的数据按GDP降序排序，并赋值给新字典
    sorted_dict[year] = sorted(data_dict[year], key=lambda element: element[1], reverse=True)
import json
import json
print(json.dumps(sorted_dict, ensure_ascii=False, indent=2))

# 取最新年份并输出前八名
latest_year = sorted_years[-1]
top_8 = sorted_dict[latest_year][:8]
print(f"{latest_year}年GDP前八名国家：")
for country, gdp in top_8:
    print(f"{country}: {gdp}")
# 取前八名可以在此处继续处理 latest_year 的数据

#for循环每一年的数据，基于每一年的数据，创建每一年的bar对象，并将每一年的bar对象添加到时间线中        
from pyecharts.charts import Bar,Timeline
bar = Bar()
timeline = Timeline()




