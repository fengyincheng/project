#a = 13
#a = a + 13
#a +=12
"""#a = "世界上怎么会"
from idna.compat import nameprep

name = 2.33333
b = "世界上怎么会有我黄舒宇这么伟大的人%3.2f"%name
#b = f"有我黄舒宇这么伟大的人{name}"
#c = "233333"
print(b)
d = 12
print(f"{d}的类型是：{type(d)}")"""
from itertools import count
"""
user_name = input("您好：")
user_type = ("sssssvip")
print("欢迎！",user_name,",尊贵的",user_type)"""

"""
print("欢迎来到游乐场，儿童票免费，成人票收费")
age = int(input("请输入你的年龄:"))
if age >= 18:
    print("您已成年,需补票三十元")
else:print("您是儿童，可以免费游玩")
print("祝您游玩愉快！")"""

"""
print("欢迎来到咪咪乐园！")
# visiter_height = int(input("请输入您的身高："))
# visiter_level = int(input("请输入您的vip等级：") >= 5:
# if visiter_height <= 130:
if int(input("请输入您的身高："))<= 120:
    print("...")
elif int(input("请输入您的vip等级："))>= 5:
    print("》》》")
"""

# print("猜猜谁是世界上最伟大的人？")
# if input("速速回答！") =="黄舒宇" :
#     print("算你识向^_^")
# elif input("最后一次机会（死亡警告）")== "黄舒宇":
#       print("很好，这次算你过关了")
# else:
#     print("你完了。")


# import random
# num = random.randint(1,10)
# print("来猜数字")
# gass_num = int (input())
#
# if gass_num==num:
#     print("运气真好啊你")
# else:
#     if gass_num < num:
#         print("小了，再来")
#     else:
#         print("大了，再来")
#     gass_num = int(input())
#     if gass_num == num:
#       print("对了")
#     else:
#           if gass_num < num:
#               print("小了")
#           else:print("大了")
#
#
#           gass_num = int(input("最后一次了"))
#           if gass_num == num:
#               print("gongxi")
#           else:print("youxishibai")

# s = 1
# i = 0
#
# while i <= 100:
#     s = s + i
#     i += 1
#     print(s)

# import random
# tru_num = random.randint(1,20);count=1
# print("猜数字")
# guess_num = 0
# while guess_num != tru_num:
#     guess_num = int(input("再来！"))
#     count +=1
#     if guess_num > tru_num:
#         print("大了")
#     if guess_num < tru_num:
#         print("小了")
# else:
#     print("恭喜，你一共猜了",count,"次")

# i = 1
# while i <= 9:
#     j = 1
#     while j <= i:
#         print(f"{j}*{i}={i*j}/t",end='' )
#         j += 1
#     i = i + 1
#     print()



# name = "huangshuyu"
# j = 0
# for x in name:
#
#     if x == "u":
#         j +=1
# print(f"huangshuyu共有{j}个u")

# count = 0
# for x in range(1,100):
#     if x % 2 == 0:
#         count += 1
# print(count)


#乘法表
# for i in range(1,10):
#     for j in range(1,i+1):#曾经我这里写的是range（1，10）
#         print(f"{i}*{j}={i*j}/t",end=" ")
#     print()
"""
mony = 10000
for i in range(1,51):
    import random
    number = random.randint(1,10)
    if mony > 1000:
        mony = mony - 1000
    else:
     print("没钱了")
     break

    if number >= 5:
        print(f"员工{i}绩效达标，领取工资。")
    else:
        print(f"员工{i}绩效不达标，没钱拿")
        
"""




# def imput(i):
#     print("hello world\nUser!\n请输入您的用户ID：")
#
#     if i > 1000:
#         print("ID过长")
#     else:
#         print("欢迎登录！")
# imput(1001)



# name = input("请输入您的姓名：")
# mony = 10000
# print(name)
# def main():
#     print("--------主菜单---------")
#     print(f"{name}您好！欢迎来到咪咪银行！请选择操作：")
#     print(f"查询余额 输入{1}\n取款 输入{3}\n存入 输入{2}\n退出 输入{4}")


# def check_mony():

#     print(f"您的余额是:{mony}")

# def save_mony(i):
#     i = int(input("请输入存入金额："))
#     print(i)
#     global mony
#     mony += i

# def take_mony(x):
#     x = int(input("请输入取款金额："))
#     print(x)
#     global mony
#     mony -= x




# while True:
#     main()
#     s = int(input("请输入您的操作："))
#     print(s)
#     if s == 1:
#         check_mony()
#         continue
#     elif s == 3:
#         save_mony(i)
#         continue
#     elif s == 2:
#         take_mony()
#         continue
#     else:
#         break


"""
#列表的基本操作

#追加元素
my_list = ["黄舒宇","张三","李四","王五","张三","张三"]

my_list2 = ["赵六","钱七"]
my_list.extend(my_list2)

#删除元素
del my_list[0]
my_list.pop(1)
print(my_list)

#移除元素

print(f"被移除的元素是{my_list.pop(1)}")


my_list.remove("张三")
print(f"移除张三后的列表：{my_list}")

#插入元素
my_list.insert(1,"gui")
print(f"插入元素后的列表：{my_list}")

#查找元素位置
my_list.index("张三")
print(f"张三的位置在：{my_list.index("张三")}")

#统计单一元素个数
print(f"张三出现的次数是：{my_list.count("张三")}")

#统计所有元素的个数
print(f"列表中所有元素的个数是：{len(my_list)}")

#清空列表
my_list.clear()
print(f"清空列表后：{my_list}")



"""


# my_list = [1,2,3,4,5,6,7,8,9,10]

# index = 0
# my_list2 = []

# while index < len(my_list):
#     if my_list[index] % 2 == 0:     #index即控制循环，也可以表示列表中元素的下标，以达到从列表中取值的目的
#         my_list2.append(my_list[index])  #append()方法用于在列表末尾添加新的元素，这里将偶数添加到新的空列表中
      
#     index += 1
# print(f"偶数列表是：{my_list2}")

# for x in my_list:
#     if x % 2 == 0:
#         my_list2.append(x)
# print(f"偶数列表是：{my_list2}")

"""
t1 = (1,2,3,4,[5,6,7])
t1[-1].append(8)
print(t1)
t1[-1][0] = 9
print(t1)
count = t1.count (3)
print(count)
index = t1.index(4)
print(index)
len_t1 = len(t1)
print(len_t1)

"""

#     #字典的基本操作
# my_dict = {
#     "小白":{"级别":1,"工资":3000},
#     "小黑":{"级别":2,"工资":4000},
#     "小黄":{"级别":3,"工资":5000},  #字典的嵌套
#     "小绿":{"级别":1,"工资":6000}
# }
# for key in my_dict:
#     if my_dict[key]["级别"] == 1:
#         my_dict[key]["级别"] += 1
#         my_dict[key]["工资"] += 1000
#         x = my_dict 
# print(f"曾经{my_dict}现在是{x}")
# #字典的删除


def compose(f,g):
    def h(x):
        return f(g(x))
    return h
  
g = lambda x: x + 6
f = lambda g: g * 2

print ( compose(f,g)(2))




# with open(r"C:/Users/Lenovo/Desktop/测试.txt", "r", encoding="utf-8") as x:
#         content = x.read()
#         y = content.count("当")
#         print(f"文本中当字出现的次数是：{y}")
        

# import time
# print("hhhh")
# time.sleep(2)
# print("wwww")


"""
import my_mod
print(my_mod.my_mod(10,2))

"""


