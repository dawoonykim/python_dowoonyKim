# 프로그래머스 부분 문자열

def solution(str1, str2):
    answer = 0
    if str1 in str2:
        answer = 1
    else:
        answer = 0
    return answer


print(solution("abc", "abccc"))
print(solution("tbt", "tbbttb"))
