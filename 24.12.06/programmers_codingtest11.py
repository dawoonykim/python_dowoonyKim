# 프로그래머스 - n보다 커질 때까지 더하기

def solution(numbers, n):
    answer = 0
    for i in numbers:
        if n >= answer:
            answer += i
    return answer


print(solution([34, 5, 71, 29, 100, 34], 123))
print(solution([58, 44, 27, 10, 100], 139))
