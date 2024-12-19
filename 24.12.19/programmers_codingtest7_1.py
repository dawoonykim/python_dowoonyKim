# 프로그래머스 - 소인수 분해

def solution(n):
    answer = set()
    i = 2
    while n > 1:
        while n % i == 0:
            answer.add(i)
            n /= i
        i += 1
    return answer


print(solution(12))
print(solution(17))
print(solution(420))
