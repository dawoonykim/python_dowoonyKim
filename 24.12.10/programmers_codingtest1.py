# 프로그래머스 - 특별한 이차원 배열 1

def solution(n):
    answer = []

    for i in range(n):
        line = []
        for j in range(n):
            if i == j:
                line.append(1)
            else:
                line.append(0)
        answer.append(line)
    return answer


print(solution(3))
print(solution(6))
print(solution(1))
