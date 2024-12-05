def oneUp():
    global x
    x += 1
    return x


x = 0
print(oneUp())
print(oneUp())
print(oneUp())

# def oneUp():
#     # global x
#     x += 1 # 할당인지 선언인지 구분이 안되기 때문에 에러 발생
             # 선언과 할당이 구분되어 있지 않음 => 지역 변수인데, 선언과 할당이 한 번에 이뤄지면 에러가 발생함
#     return x


# x = 0
# print(oneUp())
# print(oneUp())
# print(oneUp())
