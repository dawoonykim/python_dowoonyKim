# 프로그래머스 - 빈 배열에 추가, 삭제하기

def solution(arr, flag):
    answer = []
    for i in range(len(flag)):
        if flag[i] == True:
            for j in range(2*arr[i]):
                answer.append(arr[i])
        else:
            for j in range(arr[i]):
                answer.pop()
    return answer


print(solution([3, 2, 4, 1, 3], [True, False, True, False, False]))
