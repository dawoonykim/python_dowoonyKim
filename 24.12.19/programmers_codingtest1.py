# 프로그래머스 - 다항식 더하기

def solution(polynomial):
    print(type(polynomial))
    polynomial = polynomial.split(" + ")
    
    num = 0  # 다항식
    sum = 0  # 상수

    for term in polynomial:
        if "x" in term:
            if len(term) > 1:
                num += int(term[:-1])
            else:
                num += 1
        else:
            sum += int(term)

    if num == 0:
        # print(1)
        return f"{sum}"
    elif num == 1:
        # print(2)
        if sum == 0:
            # print(3)
            return f"x"
        elif sum != 0:
            # print(4)
            return f"x + {sum}"
    elif num > 1:
        if sum == 0:
            # print(5)
            return f"{num}x"
        else:
            # print(6)
            return f"{num}x + {sum}"


print(solution("3x + 7 + x"))
print(solution("x + x + x"))
