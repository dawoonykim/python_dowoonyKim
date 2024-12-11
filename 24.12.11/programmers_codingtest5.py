# 프로그래머스 - 세균증식

def solution(n, t):
    answer = n
    for i in range(1, t+1):
        answer *= 2
    return answer


print(solution(2, 10))
print(solution(7, 15))
