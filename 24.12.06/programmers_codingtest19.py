# 프로그래머스 - 배열에서 문자열 대소문자 변환하기
def solution(strArr):
    for i in range(len(strArr)):
        if i % 2 == 0:
            strArr[i] = strArr[i].lower()
        else:
            strArr[i] = strArr[i].upper()

    return strArr


print(solution(["AAA", "BBB", "CCC", "DDD"]))
print(solution(["aBc", "AbC"]))
