# 프로그래머스 - 문자열 묶기

def solution(strArr):
    answer = 0
    answer_li = {}
    for i in strArr:
        length = len(i)
        if length not in answer_li:
            answer_li[length] = []
        answer_li[length].append(i)

    for i in answer_li:
        answer = max(len(v) for v in answer_li.values())

    print(answer_li)
    return answer


print(solution(["a", "bc", "d", "efg", "hi"]))
