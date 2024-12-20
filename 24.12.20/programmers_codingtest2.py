# 프로그래머스 - 배열 회전시키기

def solution(numbers, direction):
    answer = []
    if direction == "right":
        answer.append(numbers[-1])
        for i in range(len(numbers)-1):
            answer.append(numbers[i])
    elif direction == "left":
        for i in range(1, len(numbers)):
            answer.append(numbers[i])
        answer.append(numbers[0])

    return answer


print(solution([1, 2, 3], "right"))
print(solution([4, 455, 6, 4, -1, 45, 6], "left"))
