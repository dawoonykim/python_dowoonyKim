# 프로그래머스 - 두 개 뽑아서 더하기

def solution(numbers):
    answer = []
    answer_s = set()
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            answer_s.add(numbers[i]+numbers[j])

    answer = list(answer_s)
    answer.sort()
    return answer


print(solution([2, 1, 3, 4, 1]))
print(solution([5, 0, 2, 7]))
