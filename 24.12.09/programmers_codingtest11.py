# 프로그래머스 - 문자열 정수의 합

def solution(num_str):
    answer = 0
    li = list(map(int, num_str))
    print(li)
    for i in li:
        answer+=i
    return answer


print(solution("123456789"))
print(solution("1000000"))
