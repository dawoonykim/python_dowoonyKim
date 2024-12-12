# 프로그래머스 - 암호 해독

def solution(cipher, code):

    li = list(cipher[code-1::code])
    return "".join(li)


print(solution("dfjardstddetckdaccccdegk", 4))
print(solution("pfqallllabwaoclk", 2))
