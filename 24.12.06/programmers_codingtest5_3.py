# 프로그래머스 - 왼쪽 오른쪽

def solution(str_list):
    if "l" in str_list:
        l = str_list.index("l")
    else:
        l = 0
    if "r" in str_list:
        r = str_list.index("r")
    else:
        r = 0
    
    if l>r:
        return str_list[r+1:]
    elif r>l:
        return str_list[:l]
    else:
        return []

        


print(solution(["u", "u", "l", "r"]))
print(solution(["l"]))
