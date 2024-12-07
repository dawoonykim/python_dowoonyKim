# 프로그래머스 - ad 제거하기

def solution(strArr):
    return [x for x in strArr if "ad" not in x]

print(solution(["and", "notad", "abcd"]))
print(solution(["there", "are", "no", "a", "ds"]))
