# 프로그래머스 - 문자열 밀기

def solution(A, B):
    answer = 0
    temp = ""
    li = list(A)

    for _ in range(len(A)):
        if A == B:
            return answer
        answer += 1
        temp = li.pop()
        A = temp+"".join(li)
        li=list(A)
        print(A)
    return -1


print(solution("hello", "ohell"))
print(solution("apple", "elppa"))
print(solution("atat", "tata"))
print(solution("abc", "abc"))
