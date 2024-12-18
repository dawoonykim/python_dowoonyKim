# 프로그래머스 - 숨어있는 숫자의 덧셈 (2)


def solution(my_string):
    li = []
    word = ""
    for i in my_string:

        if i.isdigit():
            word += i
        else:
            if word:
                li.append(word)
                word = ""
    if word:
        li.append(word)

    return sum(map(int, li))


print(solution("aAb1B2cC34oOp"))
print(solution("1a2b3c4d123Z"))
