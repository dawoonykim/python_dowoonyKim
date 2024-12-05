# 프로그래머스 - 글자 지우기

def solution(my_string, indices):
    answer = ''
    str_list = []
    for i in my_string:
        str_list.append(i)
    for i in indices:
        # print(my_string[i])
        str_list[i] = ""

    str_list = list(filter(None, str_list))
    print(str_list)
    for i in str_list:
        answer += i
    return answer


print(solution("apporoograpemmemprs", [1, 16, 6, 15, 0, 10, 11, 3]))
