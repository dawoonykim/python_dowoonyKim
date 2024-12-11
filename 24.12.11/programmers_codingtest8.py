# 프로그래머스 - OX퀴즈

def solution(quiz):
    q_li = []
    answer = []
    for str in quiz:
        q_li.append(str.split(" = "))

    for i in range(len(q_li)):
        for j in range(len(q_li[i])):
            q_li[i][j] = eval(q_li[i][j])
        if q_li[i][0] == q_li[i][1]:
            answer.append("O")
        else:
            answer.append("X")
    return answer


print(solution(["3 - 4 = -3", "5 + 6 = 11"]))
print(solution(["19 - 6 = 13", "5 + 66 = 71", "5 - 15 = 63", "3 - 1 = 2"]))
