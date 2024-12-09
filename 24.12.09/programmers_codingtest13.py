# 프로그래머스 - 0 떼기

def solution(n_str):
    answer = ''
    li = list(n_str)
    i = 0

    for j in li:
        if j != "0":
            break
        i += 1

    for j in li[i:]:
        answer += j
    return answer


print(solution("0010"))
print(solution("854020"))
