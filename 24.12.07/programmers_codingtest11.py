# 프로그래머스 - 세 개의 구분자

def solution(myStr):
    answer = []
    start = 0
    count = 0
    for i in range(len(myStr)):
        str = ""
        if "a" == myStr[i] or "b" == myStr[i] or "c" == myStr[i]:
            start += 1
        else:
            answer.append(myStr[start:count+start])
            count += 1
        if len(answer) == 0:
            answer.append("EMPTY")
    return answer


print(solution("baconlettucetomato"))
print(solution("abcd"))
print(solution("cabab"))
