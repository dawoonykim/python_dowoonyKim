# 프로그래머스 문자열 여러 번 뒤집기
def solution(my_string, queries):
    
    for i in queries:
        s = i[0]
        e = i[1]
        
        # my_string=my_string.replace(my_string[s:e+1],"".join(my_string[s:e+1])[::-1])
        # my_string[s:e+1][::-1] : 원하는 부분을 슬라이싱해서 거꾸로 뒤집기
        my_string=my_string[:s]+my_string[s:e+1][::-1]+my_string[e+1:]

    return my_string


print(solution("rermgorpsam", [[2, 3], [0, 7], [5, 9], [6, 10]]))
