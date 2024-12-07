# 프로그래머스 - 추억 점수

def solution(name, yearning, photo):
    answer = []
    dic = dict(zip(name, yearning))
    # print(dic)

    for i in range(len(photo)):
        sum = 0
        for j in range(len(photo[i])):
            if photo[i][j] in dic:
                sum+=dic[photo[i][j]]
        answer.append(sum)
    return answer


print(solution(["may", "kein", "kain", "radi"], [5, 10, 1, 3], 
               [["may", "kein", "kain", "radi"], ["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]))
print(solution(["kali", "mari", "don"], [11, 1, 55], [
      ["kali", "mari", "don"], ["pony", "tom", "teddy"], ["con", "mona", "don"]]))
print(solution(["may", "kein", "kain", "radi"], [5, 10, 1, 3],
      [["may"], ["kein", "deny", "may"], ["kon", "coni"]]))
