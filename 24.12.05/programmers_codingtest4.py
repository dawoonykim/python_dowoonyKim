# 프로그래머스 - 세로 읽기

def solution(my_string, m, c):
    answer = ''
    answer_list = []

    for i in range(len(my_string)//m):
        answer_list.append(my_string[i*m:(i+1)*m])
    print(answer_list)

    for i in answer_list:
        # answer +=
        answer += i[c-1]
    return answer


print(solution("ihrhbakrfpndopljhygc", 4, 2))
print(solution("programmers", 1, 1))
