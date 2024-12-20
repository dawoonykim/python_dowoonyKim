# 프로그래머스 - 배열 회전시키기

def solution(numbers, direction):
    answer = []
    if direction == "right":
        answer = [numbers[-1]]+numbers[:-1]
    elif direction == "left":
        answer = numbers[1:]+[numbers[0]]

    return answer


print(solution([1, 2, 3], "right"))
print(solution([4, 455, 6, 4, -1, 45, 6], "left"))
