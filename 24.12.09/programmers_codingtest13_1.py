# 프로그래머스 - 0 떼기

def solution(n_str):
    return n_str.lstrip("0")
    # return n_str.rstrip("0")


print(solution("0010"))
print(solution("854020"))
