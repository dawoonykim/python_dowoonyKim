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
    elif len(counter) == 2:
        p, q = counter.keys()
        answer = (p+q)*abs(p-q)
    elif len(counter) == 3 and 2 in counter.values():
        diffrent = [k for k, v in counter.items() if v == 1]
        answer = diffrent[0]*diffrent[1]
    else:
        min_v=min([a,b,c,d])
        answer=min_v
    return answer


print(solution(2, 2, 2, 2))
print(solution(4, 1, 4, 4))
print(solution(6, 3, 3, 6))
print(solution(2, 5, 2, 6))
print(solution(6, 4, 2, 5))
