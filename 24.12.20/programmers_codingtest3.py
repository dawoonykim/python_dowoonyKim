# 프로그래머스 - 공 던지기

def solution(numbers, k):
    answer = []
    numbers += numbers+numbers
    i = 0
    count = 0
    while count < k:
        answer.append(numbers[i])
        i += 2
        count += 1
    # print(numbers)
    # print(answer)

    return answer[-1]


print(solution([1, 2, 3, 4], 2))
print(solution([1, 2, 3, 4, 5, 6], 5))
print(solution([1, 2, 3], 3))
