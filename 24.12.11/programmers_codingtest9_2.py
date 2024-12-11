# 프로그래머스 - 자릿수 더하기

def solution(n):
    li = list(map(int, str(n)))
    return sum(li)


print(solution(1234))
print(solution(930211))
