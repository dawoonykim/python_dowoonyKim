# 프로그래머스 - 뒤에서 5등 위로

def solution(num_list):
    answer = num_list
    answer.sort()
    return answer[5::]


print(solution([12, 4, 15, 46, 38, 1, 14, 56, 32, 10]))