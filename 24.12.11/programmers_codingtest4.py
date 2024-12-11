# 프로그래머스 - 문자열 정렬하기 2

def solution(my_string):
    answer = my_string.lower()
    li = list(answer)
    li.sort()
    answer = "".join(li)
    return answer


print(solution("Bcad"))
print(solution("heLLo"))
print(solution("Python"))
