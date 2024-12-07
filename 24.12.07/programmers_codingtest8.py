# 프로그래머스 - 간단한 식 계산하기

def solution(binomial):
    # str = binomial.split()
    # print(str)
    # binomial = "".join(str)
    answer = eval(binomial)
    return answer


print(solution("43 + 12"))
print(solution("0 - 7777"))
print(solution("40000 * 40000"))
