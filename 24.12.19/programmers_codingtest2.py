# 프로그래머스 - 최댓값 만들기 (2)

def solution(numbers):
    answer = 0
    li = set()
    count = 0
    for i in range(len(numbers)):
        for j in range(1+count, len(numbers)):
            li.add(numbers[i]*numbers[j])
        count += 1

    return sorted(li)[-1]


print(solution([1, 2, -3, 4, -5]))
print(solution([0, -31, 24, 10, 1, 9]))
print(solution([10, 20, 30, 5, 5, 20, 5]))
