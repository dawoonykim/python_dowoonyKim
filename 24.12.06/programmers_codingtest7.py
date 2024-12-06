# 프로그래머스 - n개 간격의 원소들

def solution(num_list, n):
    answer = num_list[::n]
    return answer


print(solution([4, 2, 6, 1, 7, 6], 2))
print(solution([4, 2, 6, 1, 7, 6], 4))
