# 프로그래머스 - 직사각형 넓이 구하기

def solution(dots):
    answer = 0
    dots.sort()
    print(dots)
    x = abs(dots[0][0]-dots[2][0])
    y = abs(dots[0][1]-dots[1][1])
    return x*y


print(solution([[1, 1], [2, 1], [2, 2], [1, 2]]))
print(solution([[-1, -1], [1, 1], [1, -1], [-1, 1]]))
