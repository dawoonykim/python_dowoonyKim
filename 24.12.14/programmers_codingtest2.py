# 프로그래머스 - 유한소수 판별하기

def solution(a, b):

    diff1 = b/a
    print(f"diff1 : {diff1}")
    diff2 = b//a
    print(f"diff2 : {diff2}")
    if diff1 == diff2:
        if diff1 % 2 == 0 or diff1 % 5 == 0:
            return 1
    elif diff1 != diff2 and b % 2 == 0 and b % 5 == 0:
        return 1
    else:
        return 2


print(solution(7, 20))
print(solution(11, 22))
print(solution(12, 21))
