my_list = [["a",13],["b",55],["c",11]]
# def sort_key(element):
#     return element[1]


# my_list.sort(key=sort_key,reverse=True)
# print(my_list)

my_list.sort(key=lambda element : element[1],reverse=True)
print(my_list)