# 프로그래머스 - 2의 영역

def solution(arr):
    answer = []
    index = []
    for i in range(len(arr)):
        if arr[i] == 2:
            index.append(i)

    if len(index) == 0:
        answer.append(-1)
    else:
        answer = arr[index[0]:index[-1]+1]
    return answer


print(solution([1, 2, 1, 4, 5, 2, 9]))
print(solution([1, 2, 1]))
print(solution([1, 1, 1]))
print(solution([1, 2, 1, 2, 1, 10, 2, 1]))
