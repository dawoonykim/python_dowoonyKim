# def f(x):
#     result = x**2+2*x+1
#     return result


# print(f(3))


# def sayHi():
#     print("hi")
#     print("hi")
#     print("hi")


# sayHi()

x = 10  # 전역변수


def func2():
    print("func2", x)


def func():
    x = 20  # 지역변수
    y = 11
    print("func", x, y)
    func2()


func()
print("main", x)
# print("main", y)


def func3(x):
    print("func3", x)

func3(3)
