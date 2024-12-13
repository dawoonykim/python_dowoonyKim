# 프로그래머스 - A로 B 만들기기
def solution(before, after):
    li = list(after)
    for i in range(len(before)):
        if before[i] in li:
            index = li.index(before[i])
            del li[index]
        elif before[i] not in li:
            return 0
    return 1


print(solution("hello", "olleh"))
print(solution("allpe", "apple"))
