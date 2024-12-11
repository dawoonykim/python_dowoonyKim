# 프로그래머스 - 숫자 찾기

def solution(num, k):
    li = list(map(int, str(num)))
    if k in li:
        return li.index(k)+1
    else:
        return -1


print(solution(29183, 1))
print(solution(232443, 4))
print(solution(123456, 7))
