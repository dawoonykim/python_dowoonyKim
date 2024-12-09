# 프로그래머스 - 배열의 길이를 2의 거듭제곱으로 만들기

def solution(arr):
    answer = arr

    square = 1
    while square < len(arr):
        square *= 2

    for i in range(square-len(arr)):
        answer.append(0)
    print(f"square : {square}")
    return answer


print(solution([1]))
print(solution([1, 2, 3]))
print(solution([1, 2, 3, 4, 5, 6]))
print(solution([58, 172, 746, 89]))
