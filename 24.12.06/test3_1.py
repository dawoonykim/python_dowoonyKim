# 프로그래머스 x 사이의 개수

def solution(myString):
    answer = []
    str = list(myString.split("x"))
    for i in str:
        answer.append(len(i))
    return answer


print(solution("oxooxoxxox"))
print(solution("xabcxdefxghi"))
