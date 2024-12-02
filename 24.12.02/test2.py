num1 = int(input("숫자를 입력하세요."))

if num1 % 2 == 1:
    print("홀수")
if num1 % 2 == 0:
    print("짝수")

if num1 == (num1//2)*2:
    print("짝수")
if num1 != (num1//2)*2:
    print("홀수")

# else 사용
if num1 % 2 == 1:
    print("홀수")
else:
    print("짝수")

if num1 == (num1//2)*2:
    print("짝수")
else:
    print("홀수")
