# 프로그래머스 - 모음 제거

def solution(my_string):
    answer = ''.join(i for i in my_string if not (
        i in "aioue"))
    return answer


print(solution("bus"))
print(solution("nice to meet you"))
