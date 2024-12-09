# 프로그래머스 - 날짜 비교하기

def solution(date1, date2):
    answer = 0
    li = []
    for i in range(len(date1)):
        if date1[i]-date2[i] < 0:
            li.append(date1[i]-date2[i])

    if len(li) == 0 or li[0] >= 0:
        return 0
    else:
        return 1


print(solution([2021, 12, 28], [2021, 12, 29]))
print(solution([1024, 10, 24], [1024, 10, 24]))
