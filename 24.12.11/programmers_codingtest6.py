# 프로그래머스 - 제곱 수 판별하기
import math

def solution(n):
    
    num1=math.sqrt(n)
    num2=int(math.sqrt(n))

    if num1==num2:
        return 1
    else:
        return 2


print(solution(144))
print(solution(976))
