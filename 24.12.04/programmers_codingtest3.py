# 프로그래머스 오답
def solution(a, b, c, d):
    answer = 0

    if a == b == c == d:
        p = a
        answer = 1111*p
    elif a == c == d:
        p = a
        q = b
        answer = (10*p+q)**2
    elif a == d and b == c:
        p = a
        q = b
        if p-q > 0:
            answer = (p+q)*(p-q)
        else:
            answer = (p+q)*(-(p-q))
    elif a == c:
        list1 = [a, b, c, d]
        list1.remove(a)
        list1.remove(c)
        answer = list1[0]*list1[1]
    else:
        answer = min([a, b, c, d])

    return answer


print(solution(2, 2, 2, 2))
print(solution(4, 1, 4, 4))
print(solution(2, 5, 2, 6))
print(solution(6, 4, 2, 5))
