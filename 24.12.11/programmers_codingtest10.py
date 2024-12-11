# 프로그래머스 - n의 배수 고르기

def solution(n, numlist):
    answer = []
    for i in numlist:
        if i%n==0:
            answer.append(i)
    return answer


print(solution(3, [4, 5, 6, 7, 8, 9, 10, 11, 12]))
print(solution(5, [1, 9, 3, 10, 13, 5]))
print(solution(12, [2, 100, 120, 600, 12, 12]))
