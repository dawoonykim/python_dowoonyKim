# 프로그래머스 - 삼각형의 완성조건 (2)

def solution(sides):

    M, m = max(sides), min(sides)

    li1 = []
    li2 = []
    # print(max_v, min_v)

    for i in range(1, M+1):
        if m+i > M and i <= M:
            li1.append(i)
    # print(len(li1))

    for i in range(1, M+m):
        if M < i < M+m:
            li2.append(i)
    # print(li2)

    return len(li1)+len(li2)


print(solution([1, 2]))
print(solution([3, 6]))
print(solution([11, 7]))
