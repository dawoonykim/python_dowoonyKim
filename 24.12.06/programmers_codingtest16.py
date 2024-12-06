# 프로그래머스 - 원하는 문자열 찾기

def solution(myString, pat):
    patlow=pat.lower()
    myStringlow=myString.lower()
    if patlow in myStringlow:
        return 1
    else:
        return 0
  


print(solution("AbCdEfG","aBc"))
print(solution("aaAA","aaaaa"))
