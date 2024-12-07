# 프로그래머스 - 세 개의 구분자

def solution(arr):
    answer = []
    for i in range(len(arr)):
        for j in range(arr[i]):
            answer.append(arr[i])
    return answer

print(solution([5, 1, 4]))
print(solution([6, 6]))
print(solution([1]))
