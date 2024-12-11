# 프로그래머스 - 7의 개수

def solution(array):
    answer = 0

    for data in array:
        answer += str(data).count("7")
    return answer


print(solution([7, 77, 17]))
print(solution([10, 29]))
