# 프로그래머스 - ad 제거하기

def solution(strArr):
    answer = []
    for i in strArr:
        if "ad" not in i:
            answer.append(i)
    return answer


print(solution(["and", "notad", "abcd"]))
print(solution(["there", "are", "no", "a", "ds"]))
