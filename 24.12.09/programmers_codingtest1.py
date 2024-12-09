# 프로그래머스 - 배열 만들기 3

def solution(arr):
    answer = []

    for i in range(len(arr)):
        if not answer:
            answer.append(arr[i])
        elif answer and arr[i] == answer[-1]:
            answer.pop()
        elif answer and arr[i] != answer[-1]:
            answer.append(arr[i])
        # print(answer)
    if not answer:
        answer.append(-1)
    return answer


print(solution([0, 1, 1, 1, 0]))
print(solution([0, 1, 0, 1, 0]))
print(solution([0, 1, 1, 0]))
