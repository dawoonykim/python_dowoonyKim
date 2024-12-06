# 프로그래머스 - 홀수 vs 짝수

def solution(num_list):

    return max(sum(num_list[::2]),sum(num_list[1::2]))
    # return max(sum(num_list[::2]),sum(num_list[1::2]))


print(solution([4, 2, 6, 1, 7, 6]))
print(solution([-1, 2, 5, 6, 3]))
