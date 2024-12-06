# 프로그래머스 - 왼쪽 오른쪽

def solution(str_list):
    answer = []
    if ("l" and "r") in str_list:
        l_i = str_list.index("l")
        r_i = str_list.index("r")
        if l_i > r_i:
            answer = str_list[r_i:]
        else:
            answer = str_list[:l_i]
    else:
        if "l" in str_list:
            l_i = str_list.index("l")
            answer = str_list[:l_i]
        elif "r" in str_list:
            r_i = str_list.index("r")
            answer = str_list[r_i:]
    return answer


print(solution(["u", "u", "l", "r"]))
print(solution(["l"]))
