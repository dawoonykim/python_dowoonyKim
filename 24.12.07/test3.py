# 프로그래머스 - 하샤드 수

def solution(x):

    digitx = sum(map(int, str(x)))

    return x % digitx == 0


print(solution(10))
print(solution(12))
print(solution(11))
print(solution(13))
