# 프로그래머스 - 주사위 개수

def solution(box, n):
    answer = 1
    for i in box:
        answer *= i//n
    return answer


print(solution([1, 1, 1], 1))
print(solution([10, 8, 6], 3))
