# 프로그래머스 - 공 던지기
from itertools import cycle

def solution(numbers, k):
    answer = []
    cyclic_list = cycle(numbers)

    for _ in range(k):
        answer.append(next(cyclic_list))
        next(cyclic_list)
    print(answer)
    return answer[-1]


print(solution([1, 2, 3, 4], 2))
print(solution([1, 2, 3, 4, 5, 6], 5))
print(solution([1, 2, 3], 3))
