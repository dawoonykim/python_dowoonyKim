# 프로그래머스 - 종이 자르기

def solution(M, N):
    answer = 0
    for i in range(M):
        for j in range(N):
            answer += 1
    return answer-1


print(solution(2, 2))
print(solution(2, 5))
print(solution(1, 1))
