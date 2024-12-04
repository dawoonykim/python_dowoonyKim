# 프로그래머스 부분 문자열 이어 붙여 문자열 만들기
def solution(my_strings, parts):
    answer = ''
    count = 0
    for i in parts:
        s = i[0]
        e = i[1]
        answer += my_strings[count][s:e+1]
        count += 1
    return answer


print(solution(["progressive", "hamburger", "hammer",
      "ahocorasick"], [[0, 4], [1, 2], [3, 5], [7, 7]]))
