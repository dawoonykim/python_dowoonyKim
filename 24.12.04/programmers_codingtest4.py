# 프로그래머스 글자 이어붙여 문자열 만들기
def solution(my_string, index_list):
    answer = ''
    for i in index_list:
        answer += my_string[i]
    return answer


print(solution("cvsgiorszzzmrpaqpe", [16, 6, 5, 3, 12, 14, 11, 11, 17, 12, 7]))
print(solution("zpiaz", [1, 2, 0, 0, 3]))