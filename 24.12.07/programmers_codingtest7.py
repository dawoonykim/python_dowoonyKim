# 프로그래머스 - 문자열 잘라서 정렬하기

def solution(myString):
    answer = myString.split("x")
    answer = [x for x in answer if "" != x]

    answer.sort()
    return answer


print(solution("axbxcxdx"))
print(solution("dxccxbbbxaaaa"))
