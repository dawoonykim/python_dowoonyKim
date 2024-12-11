# 프로그래머스 - 약수 구하기

def solution(n):
    answer = []
    for i in range(1, n+1):
        if n % i == 0:
            answer.append(i)
    return answer

print(solution(24))
print(solution(29))