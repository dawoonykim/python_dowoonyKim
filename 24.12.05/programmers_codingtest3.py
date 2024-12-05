# 프로그래머스 - 문자열 뒤집기

def solution(my_string, s, e):
    answer = ''
    # answer += my_string[:s]+my_string[s:e+1][::-1]+my_string[e+1:]
    answer=my_string.replace(my_string[s:e+1],"".join(my_string[s:e+1][::-1]))
    return answer


print(solution("Progra21Sremm3", 6, 12))
print(solution("Stanley1yelnatS", 4, 10))
