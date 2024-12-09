# 프로그래머스 - 두 수의 합

def solution(a, b):
    ab_str = a+"+"+b
    answer = str(eval(ab_str))
    
    return answer


print(solution("582", "734"))
print(solution("18446744073709551615", "287346502836570928366"))
print(solution("0", "0"))
