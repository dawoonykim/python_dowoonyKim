# 프로그래머스 - l로 만들기

def solution(myString):
    answer = ''
    li = list(myString)
    for i in range(len(myString)):
        if ord(li[i]) < ord("l"):
            li[i] = li[i].replace(li[i], "l")
    answer = "".join(li)

    return answer


print(solution("abcdevwxyz"))
print(solution("jjnnllkkmm"))
