# 프로그래머스 - 가장 큰 수 찾기

def solution(array):

    max_v = max(array)
    index=array.index(max_v)
    answer = [max_v, index]
    return answer


print(solution([1, 8, 3]))
print(solution([9, 10, 11, 8]))
