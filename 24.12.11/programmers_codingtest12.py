# 프로그래머스 - 배열의 유사도

def solution(s1, s2):
    answer = 0
    for i in s1:
        for j in s2:
            if i==j:
                answer+=1
    return answer


print(solution(["a", "b", "c"],["com", "b", "d", "p", "c"]))
print(solution(["n", "omg"],["m", "dot"]))