# 프로그래머스 - 특정한 뭍자를 대문자로 바꾸기

def solution(my_string, alp):
    answer = ''
    if alp in my_string:
        answer = my_string.replace(alp, alp.upper())
    else:
        answer = my_string
    return answer


print(solution("programmers", "p"))
print(solution("lowercase", "x"))
