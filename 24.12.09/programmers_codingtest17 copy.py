# 프로그래머스 - 부분 문자열인지 확인하기

def solution(my_string, target):
    answer = 0
    setli = set()
    for i in range(len(my_string)):
        setli.add(my_string[:i+1])
        setli.add(my_string[-i:])

    li = list(setli)
    li.sort()
    print(li)
    if target in li:
        return 1
    return 0


print(solution("banana", "ana"))
print(solution("banana", "wxyz"))
