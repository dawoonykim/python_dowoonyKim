# 프로그래머스 - 크기가 작은 부분 문자열

def solution(t, p):
    answer = 0
    start = 0
    li = []
    while True:
        if len(t[start:len(p)+start]) < len(p):
            break
        else:
            li.append(t[start:len(p)+start])
        start += 1

    li = list(map(int, li))
    for i in li:
        if i <= int(p):
            answer += 1
    return answer


print(solution("3141592", "271"))
print(solution("500220839878", "7"))
print(solution("10203", "15"))
