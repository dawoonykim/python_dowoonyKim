# 프로그래머스 - 이진수 더하기
def solution(bin1, bin2):

    sum_result = int(bin1, 2)+int(bin2, 2)

    return format(sum_result, "b")


print(solution("10", "11"))
print(solution("1001", "1111"))
