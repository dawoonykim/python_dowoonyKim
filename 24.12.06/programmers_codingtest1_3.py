# 프로그래머스 - 2의 영역

def solution(arr):
    
    if 2 not in arr:
        return [-1]
    else:
        return arr[arr.index(2):len(arr)-arr[::-1].index(2)]

    


print(solution([1, 2, 1, 4, 5, 2, 9]))
print(solution([1, 2, 1]))
print(solution([1, 1, 1]))
print(solution([1, 2, 1, 2, 1, 10, 2, 1]))
