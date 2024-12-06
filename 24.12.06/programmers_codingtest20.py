# 프로그래머스 - A 강조하기
def solution(myString):
    return "".join("A" if char == "a" else char.lower() if char != "A" and char.isupper() else char for char in myString)


print(solution("abstract algebra"))
print(solution("PrOgRaMmErS"))
