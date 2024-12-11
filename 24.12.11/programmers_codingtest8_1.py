# 프로그래머스 - OX퀴즈

def solution(quiz):
    answer = []
    for str in quiz:
        a, b = str.split(" = ")

        if eval(a)==eval(b):
            answer.append("O")
        else:
            answer.append("X")

    return answer


print(solution(["3 - 4 = -3", "5 + 6 = 11"]))
print(solution(["19 - 6 = 13", "5 + 66 = 71", "5 - 15 = 63", "3 - 1 = 2"]))
