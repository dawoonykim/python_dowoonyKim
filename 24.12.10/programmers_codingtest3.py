# 프로그래머스 - 특별한 이차원 배열 2

def solution(arr):

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == arr[j][i]:
                continue
            else:
                return 0
    return 1


print(solution([[5, 192, 33], [192, 72, 95], [33, 95, 999]]))
print(solution([[19, 498, 258, 587], [63, 93, 7, 754],
      [258, 7, 1000, 723], [587, 754, 723, 81]]))
