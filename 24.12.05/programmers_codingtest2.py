# 프로그래머스 - 접두사인지 확인하기

def solution(my_string, is_prefix):
    answer = 0
    answer_list = []
    for i in range(len(my_string)):
        answer_list.append(my_string[0:i+1])
    # print(answer_list)
    answer_list.sort()
    if is_prefix in answer_list:
        answer = 1
    return answer


print(solution("banana", "ban"))
print(solution("banana", "nan"))
print(solution("banana", "abcd"))
print(solution("banana", "bananan"))
