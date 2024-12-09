# 프로그래머스 - 조건에 맞게 수열 변환하기 3

def solution(arr, k):
    answer = []

    answer = [(x*3 if k % 2 != 0 else x+k) for x in arr]
    return answer


print(solution([1, 2, 3, 100, 99, 98], 3))
print(solution([1, 2, 3, 100, 99, 98], 2))
