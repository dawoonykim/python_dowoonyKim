# 프로그래머스 x 사이의 개수

def solution(myString):
    answer = []
    count = 0
    for i in myString:
        if i != "x":
            count += 1
        else:
            answer.append(count)
            count = 0
    if count >= 0:
        answer.append(count)
    return answer


print(solution("oxooxoxxox"))
print(solution("xabcxdefxghi"))
