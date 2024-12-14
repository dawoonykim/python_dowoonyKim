# 프로그래머스 - 특이한 정렬
# 가까운 수 - https://school.programmers.co.kr/learn/courses/30/lessons/120890
# 이번 문제 - https://school.programmers.co.kr/learn/courses/30/lessons/120880?language=python3
def solution(numlist, n):
    answer = []

    while len(numlist) != 0:
        li = [abs(n-i) for i in numlist]
        min_diff = min(li)
        candidates = [numlist[i] for i in range(len(li)) if min_diff == li[i]]
        answer.append(max(candidates))
        index = numlist.index(max(candidates))
        del numlist[index]
    return answer


print(solution([1, 2, 3, 4, 5, 6], 4))
print(solution([10000, 20, 36, 47, 40, 6, 10, 7000], 30))
