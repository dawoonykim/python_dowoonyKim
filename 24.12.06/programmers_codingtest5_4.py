# 프로그래머스 - 왼쪽 오른쪽

def solution(str_list):
    for i in range(len(str_list)):
        if "l" == str_list[i]:
            return str_list[:i]
        elif "r" == str_list[i]:
            return str_list[i+1:]
    return []


print(solution(["u", "u", "l", "r"]))
print(solution(["l"]))
