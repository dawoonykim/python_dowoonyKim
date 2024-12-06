# 프로그래머스 - 왼쪽 오른쪽

def solution(str_list):
    l = 0
    r = 0
    for i in range(len(str_list)):
        if str_list[i] == "l":
            l = i
        if str_list[i] == "r":
            r = i

    if l == -1 and r == -1:
        return []
    elif r > l:
        return str_list[:l]
    elif r < l:
        return str_list[r:]
    elif ("l" or "r") in str_list:
        if "l" in str_list:
            return str_list[:l]
        else:
            return str_list[r:]



print(solution(["u", "u", "l", "r"]))
print(solution(["l"]))
