# 프로그래머스 - 길이에 따른 연산

def solution(num_list):
    answer = 0
    if len(num_list) >= 11:
        for i in num_list:
            answer += i
    elif len(num_list) <= 10:
        answer = 1
        for i in num_list:
            answer *= i

    return answer


print(solution([3, 4, 5, 2, 5, 4, 6, 7, 3, 7, 2, 2, 1]))
print(solution([2, 3, 4, 5]))
