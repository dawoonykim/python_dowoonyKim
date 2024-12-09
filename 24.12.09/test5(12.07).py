# 프로그래머스 - 옹알이

def solution(babbling):
    answer = 0
    can = ["aya", "ye", "woo", "ma"]
    for i in babbling:
        for j in can:
            idx = i.find(j)
            if idx > -1:
                print(idx, i, j)
                i = i.replace(j, "_"*len(j))
                print(idx, i, j)
        i = i.replace("_", "")
        if len(i) == 0:
            answer += 1
    return answer


print(solution(["aya", "yee", "u", "maa", "wyeoo"]))
print(solution(["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]))
