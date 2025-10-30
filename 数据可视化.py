import json
data = {"name:":"黄舒宇","age":18}
x = json.dumps(data,ensure_ascii=False)
print(f"转换成json后的文件是：{x}")

s= '{"name:": "\u9ec4\u8212\u5b87", "age":18}'
y = json.loads(s)
print(type(y))
print(y)