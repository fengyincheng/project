# class CLOCK:
#     def ring(self):
#         import winsound
#         winsound.Beep(5000,1000)
# clock_1 = CLOCK()
# clock_1.ring()  #括号
# #真好玩


class Menu:
    def __init__(self,name,age,habit):
        self.name = name
        self.age = age
        self.habit = habit

men = Menu('andy',18,"kill")

print(men.name)    # 输出: andy
print(men.age)     # 输出: 18
print(men.habit)   # 输出: kill

        
