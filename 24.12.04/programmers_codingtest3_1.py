# 프로그래머스 주사위 게임 3

from collections import Counter


def solution(a, b, c, d):
    answer = 0
    counter = Counter([a, b, c, d])

    if len(counter) == 1:
        answer = 1111*a
    elif 3 in counter.values() and 1 in counter.values():
        p = [k for k, v in counter.items() if v == 3][0]
        q = [k for k, v in counter.items() if v == 1][0]
        answer = (10*p+q)**2
    elif len(counter)==2:
        p, q = counter.keys()
        answer = abs(p-q)*(p*q)
    elif 2 in counter.values():
        same = [k for k, v in counter.items() if v == 2]
        differnt = [k for k, v in counter.items() if v == 1]
        answer = differnt[0]*differnt[1]
    else:
        answer = min([a, b, c, d])
    return answer


# 테스트
print(solution(2, 2, 2, 2))  # 출력: 8888
print(solution(4, 1, 4, 4))  # 출력: 361
print(solution(2, 5, 2, 6))  # 출력: 21
print(solution(6, 4, 2, 5))  # 출력: 2

