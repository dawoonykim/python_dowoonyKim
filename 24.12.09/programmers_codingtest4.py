# 프로그래머스 - 배열 비교하기

def solution(arr1, arr2):

    len1 = len(arr1)
    len2 = len(arr2)
    sum1 = 0
    sum2 = 0

    if len1 != len2:
        if len1 > len2:
            return 1
        else:
            return -1
    else:
        for i in range(len1):
            sum1 += arr1[i]
            sum2 += arr2[i]
        if sum1 > sum2:
            return 1
        elif sum1 < sum2:
            return -1
        else:
            return 0


print(solution([49, 13], [70, 11, 2]))
print(solution([100, 17, 84, 1], [55, 12, 65, 36]))
print(solution([1, 2, 3, 4, 5], [3, 3, 3, 3, 3]))
