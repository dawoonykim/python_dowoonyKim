# 프로그래머스 - k의 개수

def solution(i, j, k):
    answer = 0
    li = ""
    for i in range(i, j+1):
        li += str(i)

    for i in li:
        if i.count(str(k)):
            answer += 1
    return answer


print(solution(1, 13, 1))
print(solution(10, 50, 5))
print(solution(3, 10, 2))
