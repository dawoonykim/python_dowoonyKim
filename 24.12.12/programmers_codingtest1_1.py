# 프로그래머스 - 인덱스 바꾸기

def solution(my_string, num1, num2):

    li = list(my_string)
    li[num1], li[num2] = li[num2], li[num1]
    print(li)

    return "".join(li)


print(solution("hello", 1, 2))
print(solution("I love you", 3, 6))
