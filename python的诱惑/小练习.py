     #布尔值——门禁系统
# has_key = input("是否有钥匙？").lower() == "yes"
# face_match = input("人脸匹配？").lower() == "yes"
# admin_mode = input("是否是管理员模式？").lower() == "yes"
# if admin_mode == True:
#     print("门已解锁")
# elif has_key == True and face_match == True:
#     print("门已解锁")
# else:
#     print("拒绝访问")



exclent_name = []
study_habit_stiuation = {"Alice": "Good", "Bob": "Average", "Charlie": "Good"}
for name,study_habit in study_habit_stiuation.items(): #通过items()方法同时遍历键和值
    print(f"{name}的学习习惯是{study_habit}")
    if study_habit == "Good":
       
        exclent_name.extend([name])
print(f"其中拥有优秀学习习惯的是{exclent_name}") #不要把这行代码放在循环内，这样才会在最后一行输出，而非中间行
    #创建列表输出不止一个优秀学习习惯的学生姓名
