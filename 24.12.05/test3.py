# 두 수(2, 2)를 매개변수로 전달하여 서로 같으면 곱하고, 서로 다르면 더하는 함수를
# 정의하고 호출하는 프로그램을 작성하세요.

def compare1(x, y):
    result = 0

    if x == y:
        result = x*y
    else:
        result = x+y

    return result


def compare2(x, y):

    if x == y:
        print(x*y)
    else:
        print(x+y)


print(compare1(2, 2))
compare2(2, 5)
