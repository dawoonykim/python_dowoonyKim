# 프로그래머스 - 최댓값 만들기 (1)

def solution(numbers):
    numbers.sort()
    return numbers[-1]*numbers[-2]


print(solution([1, 2, 3, 4, 5]))
print(solution([0, 31, 24, 10, 1, 9]))
