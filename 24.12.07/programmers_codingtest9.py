# 프로그래머스 - 문자열 바꿔서 찾기

def solution(myString, pat):
    answer = 0
    li = list(myString)
    for i in range(len(li)):
        if li[i] == "A":
            li[i] = "B"
        elif li[i] == "B":
            li[i] = "A"
    li_str="".join(li)
    if pat in li_str:
        return 1
    return 0


print(solution("ABBAA",	"AABB"))
print(solution("ABAB", "ABAB"))
