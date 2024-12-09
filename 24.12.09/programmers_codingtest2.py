# 프로그래머스 - 무작위로 k개의 수 뽑기

def solution(arr, k):
    answer = []
    for i in range(len(arr)):
        if arr[i] not in answer and len(answer) < k:
            answer.append(arr[i])

    if len(answer) < k:
        for i in range(k-len(answer)):
            answer.append(-1)

    return answer


print(solution([0, 1, 1, 2, 2, 3], 3))
print(solution([0, 1, 1, 1, 1], 4))
