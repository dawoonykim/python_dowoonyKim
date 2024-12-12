# 프로그래머스 - 대문자와 소문자

def solution(my_string):
    answer = ''
    for i in my_string:
        if 65<=ord(i)<=90:
            answer+=i.lower()
        else:
            answer+=i.upper()
    return answer


print(solution("cccCCC"))
print(solution("abCdEfghIJ"))
