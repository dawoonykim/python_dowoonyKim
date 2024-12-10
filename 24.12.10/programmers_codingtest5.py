# 프로그래머스 - 옹알이(1)

def solution(babbling):
    answer = 0
    li = ["aya", "ye", "woo", "ma"]
    for i in range(len(li)):
        for j in range(len(babbling)):
            if li[i] in babbling[j]:
                babbling[j] = babbling[j].replace(li[i], "_"*len(li[i]))
                if "_"*len(babbling[j]) == babbling[j]:
                    answer += 1

    return answer


print(solution(["aya", "yee", "u", "maa", "wyeoo"]))
print(solution(["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]))
