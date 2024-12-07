# 프로그래머스 - 특정한 뭍자를 대문자로 바꾸기

def solution(myString, pat):
    answer = ''
    if pat in myString:
        index = myString.rfind(pat) # => rfind와 find 그리고 index를 잘 활용해보자
        print(index)
        answer = myString[:index+len(pat)]
    return answer


print(solution("AbCdEFG", "dE"))
print(solution("AAAAaaaa", "a"))
