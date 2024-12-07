# 프로그래머스 - rny_string

def solution(rny_string):
    answer = ''
    li = list(rny_string)
    for i in range(len(li)):
        if "m" == li[i]:
            li[i] = "rn"

    answer = "".join(li)
    return answer


print(solution("masterpiece"))
print(solution("programmers"))
print(solution("jerry"))
print(solution("burn"))
