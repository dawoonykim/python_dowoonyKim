# 프로그래머스 - 날짜 비교하기

def solution(date1, date2):
    for i in range(len(date1)):
        if date1[i] < date2[i]:
            return 1
        elif date1[i] > date2[i]:
            return 0
    return 0

print(solution([2021, 12, 28], [2021, 12, 29]))
print(solution([1024, 10, 24], [1024, 10, 24]))
