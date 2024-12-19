# 프로그래머스 - 팩토리얼

def solution(n):
    answer = 0
    i = 1
    count = 1
    while i <= n:
        answer = count
        count += 1
        i *= count
    return answer


print(solution(3628800))
print(solution(7))
