# 프로그래머스 - 문자열 내림차순으로 배치하기

def solution(s):
    li = list(s)
    li.sort()

    answer = ''.join(li)
    return answer[::-1]


print(solution("Zbcdefg"))
