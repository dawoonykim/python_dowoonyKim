# 프로그래머스 - 연속된 수의 합

def solution(num, total):
    answer = []
    find_center = total//num

    for i in range(find_center-(num-1)//2, find_center+(num+2)//2):
        answer.append(i)

    return answer


print(solution(3, 12))
print(solution(5, 15))
print(solution(4, 14))
print(solution(5, 5))
