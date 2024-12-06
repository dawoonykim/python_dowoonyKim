# 프로그래머스 - n 번째 원소부터

def solution(num_list, n):
    answer = []
    answer=num_list[n-1:]
    return answer

print(solution([2, 1, 6],3))
print(solution([5, 2, 1, 7, 5],2))
