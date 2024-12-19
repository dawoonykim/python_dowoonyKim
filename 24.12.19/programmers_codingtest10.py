# 프로그래머스 - 모음 제거

def solution(my_string):
    answer = ''.join(i for i in my_string if not (
        i == "a" or i == "i" or i == "o" or i == "u" or i == "e"))
    return answer


print(solution("bus"))
print(solution("nice to meet you"))
