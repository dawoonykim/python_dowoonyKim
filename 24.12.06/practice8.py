# def add(x, y): return x+y


# def add2(x, y):
#     return x+y


# print(type(add))

# print(add(1, 2))

# add3 = add2
# print(add2(1, 2))
# print(add3(1, 2))


# def call_3(func):
#     for i in range(3):
#         func()


# call_3(lambda: print("hi"))


# def download(startCallback, endendCallback):
#     startCallback()
#     # download
#     print("download 중")
#     ###
#     ###
#     endendCallback()


# download(lambda: print("다운로드 시작"), lambda: print("다운로드 완료"))


list(map(int, ["1", "2", "3"]))

result = map(lambda x: x*3, [1, 2, 3, 4])
print(list(result)) # => 일회용 함수
