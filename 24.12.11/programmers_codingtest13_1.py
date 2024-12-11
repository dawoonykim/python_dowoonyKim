# 프로그래머스 - 문자열 계산하기

def solution(my_string):
    a, b = map(int, my_string.split(" + "))
    return a + b


print(solution("3 + 4"))
