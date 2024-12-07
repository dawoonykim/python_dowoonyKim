# 프로그래머스 - 세 개의 구분자
import re


def solution(myStr):
    answer = re.split(r'[abc]+', myStr)

    answer = [x for x in answer if x]
    if len(answer) == 0:
        answer.append("EMPTY")
    return answer


print(solution("baconlettucetomato"))
print(solution("abcd"))
print(solution("cabab"))
