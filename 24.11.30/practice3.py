# a = []
# b = [1, 2, 3, 4, 5]
# c = ["장원영", "안유진"]
# d = [1, "아이브"]

# print(len(c))
# print(c[0])
# c[0] = "카리나"
# print(c)

# del c[0]
# print(c)

# c.append("로제")
# print(c)

# print(b[-1])
# print(b[-2])
# print(b[0:3])

# seasons = ["봄", "여름", "가을", "겨울"]
# print(seasons[0:1])
# print(seasons[0:2])
# print(seasons[:2])
# print(seasons[1:])
# print(seasons[2:])
# print(seasons[1:3])
# print(seasons[:])
# print(seasons[::1])
# print(seasons[::2])
# print(seasons[::3])
# print(seasons[::-1])
# reverse_season=reversed(seasons)
# print(reverse_season)
# temp = ""
# for i in range(len(b)-1):
#     temp = b[i]
#     b[i] = b[i+1]
#     b[i+1] = temp

# print(b)
seasons2 = ["봄", "여름", "가을", "겨울", [1, 2, 3, 4]]
print(seasons2[-1])
print(seasons2[-1][0])
del seasons2[-1][1:3]
print(seasons2[-1])


