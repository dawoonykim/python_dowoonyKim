# 프로그래머스 - 꼬리 문자열

def solution(str_list, ex):
    answer = ''
    for i in str_list:
        if ex not in i:
            answer += i
    return answer


print(solution(["abc", "def", "ghi"], "ef"))
print(solution(["abc", "bbc", "cbc"], "c"))
