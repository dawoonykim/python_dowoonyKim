# 프로그래머스 - 삼각형의 완성조건 (1)

def solution(sides):

    sides.sort()
    if sides[0]+sides[1]>sides[2]:
        return 1
    else:
        return 2
    


print(solution([1, 2, 3]))
print(solution([3, 6, 2]))
print(solution([199, 72, 222]))
