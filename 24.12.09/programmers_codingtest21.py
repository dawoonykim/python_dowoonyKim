# 프로그래머스 - 주사위 게임 1

def solution(a, b):
    answer = 0
    if a % 2 != 0 and b % 2 != 0:
        return a**2+b**2
    elif (a % 2 == 1 and b % 2 != 1) or (a % 2 == 0 and b % 2 != 0):
        return 2*(a+b)
    return abs(a-b)


print(solution(3, 5))
print(solution(6, 1))
print(solution(2, 4))
