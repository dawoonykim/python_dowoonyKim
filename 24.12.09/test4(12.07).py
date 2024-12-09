# 프로그래머스 - 특이한 정렬

def solution(numlist, n):
    answer = []
    d = {}

    for i in numlist:
        d[i] = abs(i-n)
    d1 = sorted(d.items(), key=lambda item: (item[1], -item[0]))
    # print(d.items)
    # print(d1)

    for i in d1:
        answer.append(i[0])

    return answer


print(solution([1, 2, 3, 4, 5, 6], 4))
print(solution([10000, 20, 36, 47, 40, 6, 10, 7000], 30))
