# 프로그래머스 - 왼쪽 오른쪽

def solution(str_list):
    l = 0
    r = 0
    for i in range(len(str_list)):
        if str_list[i] == "l":
            l = i
        if str_list[i] == "r":
            r = i

    if l != 0 and (r > l):
        return str_list[:l]
    elif r != 0 and (r < l):
        return str_list[r+1:]
    else:
        return []


print(solution(["u", "u", "l", "r"]))
print(solution(["l"]))
