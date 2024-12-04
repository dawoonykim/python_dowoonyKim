# 프로그래머스 접미사인지 확인하기

def solution(my_string, is_suffix):
    answer = 0
    answer_list = []
    for i in range(len(my_string)):
        answer_list.append(my_string[-i:])

    answer_list.sort()
    if is_suffix in answer_list:
        answer = 1
    # print(answer_list)
    return answer


print(solution("banana", "ana"))
print(solution("banana", "nan"))
print(solution("banana", "wxyz"))
print(solution("banana", "abanana"))
