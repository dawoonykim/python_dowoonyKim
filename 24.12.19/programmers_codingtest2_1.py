# 프로그래머스 - 최댓값 만들기 (2)

def solution(numbers):
    numbers.sort()

    return max(numbers[0]*numbers[1], numbers[-2]*numbers[-1])


print(solution([1, 2, -3, 4, -5]))
print(solution([0, -31, 24, 10, 1, 9]))
print(solution([10, 20, 30, 5, 5, 20, 5]))
