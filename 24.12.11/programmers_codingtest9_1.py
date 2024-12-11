# 프로그래머스 - 자릿수 더하기

def solution(n):

    return sum(list(map(int, str(n))))


print(solution(1234))
print(solution(930211))
