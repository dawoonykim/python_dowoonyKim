# 프로그래머스 - 가까운 수

def solution(array, n):
    li = [abs(i-n) for i in array]
    min_diff = min(li)
    candidates = [array[i] for i in range(len(li)) if min_diff == li[i]]
    return min(candidates)

print(solution([3, 10, 28], 20))
print(solution([10, 11, 12], 13))
