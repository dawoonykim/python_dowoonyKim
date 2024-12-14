# 프로그래머스 - 겹치는 선분의 길이

def solution(lines):
    answer = 0
    a = lines[0]
    b = lines[1]
    c = lines[2]
    print(a, b, c)
    return answer


print(solution([[0, 1], [2, 5], [3, 9]]))
print(solution([[-1, 1], [1, 3], [3, 9]]))
print(solution([[0, 5], [3, 9], [1, 10]]))
