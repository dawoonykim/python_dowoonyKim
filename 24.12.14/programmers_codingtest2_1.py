# 프로그래머스 - 유한소수 판별하기
from math import gcd


def solution(a, b):

    g = gcd(a, b)
    # print(f"최대 공약수 : {g}")
    b //= g
    # print(f"b : {b}")

    
    if b % 2 == 0 or b % 5 == 0:
        return 1
    else:
        return 2


print(solution(7, 20))
print(solution(11, 22))
print(solution(12, 21))
