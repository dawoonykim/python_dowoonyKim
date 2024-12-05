# 프로그래머스 - 문자열의 앞의 n글자

def solution(my_string, n):
    answer = ''
    # for i in range(n):
    #     answer += my_string[i]
    answer = my_string[:n]
    return answer


print(solution("ProgrammerS123", 11))
print(solution("He110W0r1d", 5))
