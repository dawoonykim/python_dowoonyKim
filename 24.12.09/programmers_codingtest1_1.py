# 프로그래머스 - 배열 만들기 3

def solution(arr):
    answer = []
    i = 0

    while len(answer) > i:
        if len(answer) == 0:
            answer.append(arr[i])
            i += 1
        elif len(answer) > 0 and arr[i] == arr[-1]:
            arr.pop()
            i += 1
        elif len(answer) > 0 and arr[i] != arr[-1]:
            arr.append(arr[i])
            i += 1
    if len(answer) == 0:
        answer.append(-1)
    return answer


print(solution([0, 1, 1, 1, 0]))
print(solution([0, 1, 0, 1, 0]))
print(solution([0, 1, 1, 0]))
