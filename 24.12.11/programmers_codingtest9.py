# 프로그래머스 - 자릿수 더하기

def solution(n):
    answer = 0
    str_length = str(n)
    for i in range(len(str_length), 0, -1):
        temp = n//10**(i-1)
        answer += temp
        n -= temp*10**(i-1)
    return answer


print(solution(1234))
print(solution(930211))
