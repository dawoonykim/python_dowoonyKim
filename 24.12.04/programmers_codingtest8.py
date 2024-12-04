# 프로그래머스 문자열의 뒤의 n글자

def solution(my_string, n):
    answer = ''
    # answer += my_string[-1:-1-n:-1]
    answer += my_string[-n:]
    return answer


print(solution("ProgrammerS123", 11))
print(solution("He110W0r1d", 5))
