# 프로그래머스 - 하노이

def solution(n):
    answer = []

    def hanoi(n, f, t, v):
        if n == 1:
            return answer.append([f, t])
        else:
            hanoi(n-1, f, v, t)
            answer.append([f, t])
            hanoi(n-1, v, t, f)

    hanoi(n, 1, 3, 2)
    return answer


print(solution(2))
