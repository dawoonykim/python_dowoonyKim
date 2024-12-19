# 프로그래머스 - 컨트롤 제트

def solution(s):
    answer = []
    s = s.split()
    # print(s)
    for i in s:
        if answer:
            if i == "Z":
                del answer[-1]
            else:
                answer.append(i)
        else:
            answer.append(i)
    return sum(map(int, answer))


print(solution("1 2 Z 3"))
print(solution("10 20 30 40"))
print(solution("10 Z 20 Z 1"))
print(solution("10 Z 20 Z"))
print(solution("-1 -2 -3 Z"))
