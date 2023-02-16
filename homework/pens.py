# with open(r'C:\Users\79535\Desktop\Python\data.txt', "r", encoding="utf-8") as file:
#     dict_new = {}
#     s = file.readlines()
#     for i in s:
#         dict_new[i.split()[0] + " " + i.split()[1]] = dict_new.get(
#             i.split()[0] + " " + i.split()[1], 0) + int(i.split()[2])
#     print(dict_new)
#     for name in sorted(dict_new):
#         print(name, dict_new.get(name))

# {'Petrov': {'envelope': 0, 'paper': 0, 'marker': 0}}