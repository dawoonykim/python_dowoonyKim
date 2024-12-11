# 프로그래머스 - 한 번만 등장한 문자

def solution(s):
    answer = ""

    for i in s:
        if s.count(i) == 1:
            answer += i
    return "".join(sorted(answer))


print(solution("abcabcadc"))
print(solution("abdc"))
print(solution("hello"))
