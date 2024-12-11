# 프로그래머스 - 문자열 안에 문자열

def solution(str1, str2):
    if str2 in str1:
        return 1
    else:
        return 2


print(solution("14ab6CDE443fgh22iJKlmn1o4", "6CD"))
print(solution("ppprrrogrammers", "pppp"))
print(solution("AbcAbcA", "AAA"))
