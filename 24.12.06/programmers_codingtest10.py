# 프로그래머스 - 할 일 목록

def solution(todo_list, finished):
    answer = []
    for i in range(len(finished)):
        if finished[i] == False:
            answer.append(todo_list[i])
    return answer


print(solution(["problemsolving", "practiceguitar", "swim", "studygraph"],[True, False, True, False]))
