# 프로그래머스 - 콜라츠 수열 만들기

def solution(n, answer=None):
    if answer is None:
        answer = []
    answer.append(n)
    if n == 1:
        return answer
    if n % 2 == 0:
        return solution(int(n/2), answer)
    else:
        return solution(n*3+1, answer)

print(solution(10))
