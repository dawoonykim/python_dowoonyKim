# 프로그래머스 - 날짜 비교하기

def solution(date1, date2):
    answer = 0
    li = []
    for i in range(len(date1)):
        li.append(date1[i]-date2[i])

    for i in li:
        if i < 0:
            answer += 1

    print(li)
    if answer > 0:
        return 1
    else:
        return 0


print(solution([2021, 12, 28], [2021, 12, 29]))
print(solution([1024, 10, 24], [1024, 10, 24]))
