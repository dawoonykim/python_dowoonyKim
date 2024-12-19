# 프로그래머스 - 배열 원소의 길이

def solution(strlist):
    answer = []
    for word in strlist:
        answer.append(len(word))
    return answer


print(solution(["We", "are", "the", "world!"]))
print(solution(["I", "Love", "Programmers."]))
