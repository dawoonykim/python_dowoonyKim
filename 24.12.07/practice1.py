def a(*numbers, b):
    print(numbers, " ", b)


a(1, 2, 3, 4, 5, b=6)
# b가 없으면 TypeError: a() missing 1 required keyword-only argument: 'b' 발생


def b():  # 함수 안에 함수 선언이 가능
    def c():
        print("c")
    c()


b()


# list => 문자열
l = ["p", "y", "t", "h", "o", "n"]
answer = "".join(l)
print(answer)  # => 리스트가 문자열로 변경됨

# 반올림 numpy를 사용하거나 int(num+0.5) 같은 형식으로 사용

# 반올림 하는 방법
num = 12.5
print(num)
num = (num/10)+0.5
print(num)
print(int(num))
num = int(num) * 10
print(num)

print(list(map(lambda x: x+3, [1, 2, 3, 4])))
print(list(map(int, input.split())))
