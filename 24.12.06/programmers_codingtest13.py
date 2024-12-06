# 프로그래머스 - 조건에 맞게 수열 변환하기2

def solution(arr):
    answer = 0
    li1 = arr.copy()
    while (True):
        for i in range(len(li1)):
            if li1[i] >= 50 and li1[i] % 2 == 0:
                li1[i] = int(li1[i]/2)
            elif li1[i] < 50 and li1[i] % 2 == 1:
                li1[i] = li1[i] * 2+1
        answer += 1
        print(f"후 {arr} {li1}")
        if arr == li1:
            return answer-1
        else:
            arr = li1.copy()


print(solution([1, 2, 3, 100, 99, 98]))
