# 프로그래머스 - 2의 영역

def solution(arr):
    answer = []
    index = []
    for i in range(len(arr)):
        if arr[i] == 2:
            index.append(i)

    count = len(index)
    if count == 0:
        answer.append(-1)
    else:
        for i in range(len(arr)):
            answer.append(arr[0:count])
    return answer


print(solution([1, 2, 1, 4, 5, 2, 9]))
print(solution([1, 2, 1]))
print(solution([1, 1, 1]))
print(solution([1, 2, 1, 2, 1, 10, 2, 1]))
