# 프로그래머스 - 정수를 나선형으로 배치하기

def solution(n):
    answer = [[0]*n for _ in range(n)]

    num = 1
    top, left = 0, 0
    bottom, right = n-1, n-1

    while num <= n*n:
        for i in range(left, right+1):
            answer[top][i] = num
            num += 1
        top += 1

        for i in range(top, bottom+1):
            answer[i][right] = num
            num += 1
        right -= 1

        for i in range(right,left-1,-1):
            answer[bottom][i]=num
            num+=1
        bottom-=1

        for i in range(bottom,top-1,-1):
            answer[i][left]=num
            num+=1
        left+=1

    return answer


print(solution(4))
print(solution(5))
