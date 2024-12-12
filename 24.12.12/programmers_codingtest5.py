# 프로그래머스 - 369게임

def solution(order):
    answer = 0
    tsn = ["3", "6", "9"]
    li = list(str(order))
    for i in li:
        if i in tsn:
            answer += 1

    return answer


print(solution(3))
print(solution(29423))
