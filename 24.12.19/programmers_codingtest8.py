# 프로그래머스 - 숨어있는 숫자의 덧셈 (1)

def solution(my_string):
    answer = 0
    for i in my_string:
        if "a"<=i<="z" or "A"<=i<="Z":
            continue
        else:
            answer+=int(i)
            
    return answer


print(solution("aAb1B2cC34oOp"))
print(solution("1a2b3c4d123"))
