li = [-5, 1, 2, -11, 76]

# value = list(filter(lambda x: x < 0, li))
# print(list(value))
# # print(value)

# value1 = list(filter(lambda x: x > 10, li))
# value2 = filter(lambda x: x > 10, li)
# # print(list(value1))
# print(list(value2))
# # print(value1)


# value3 = list(filter(lambda x: x*2 > 3, li))
# print(list(value3))

print(list(filter(lambda x: x >= 3, map(lambda x: x*2, li))))
