li = [-5, 1, 2, -11, 76]

li = list(filter(lambda x: x >= 3, map(lambda x: x*2, li)))
print(li)
