# 프로그래머스 - 최댓값 만들기 (1)

def solution(numbers):
    answer = set()
    count = 1
    for i in range(len(numbers)):
        for j in range(count, len(numbers)):
            if not numbers[i] == numbers[j]:
                answer.add(numbers[i]*numbers[j])
        count+=1
    return sorted(answer)


print(solution([1, 2, 3, 4, 5]))
print(solution([0, 31, 24, 10, 1, 9]))
