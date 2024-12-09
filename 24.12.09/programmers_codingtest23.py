# 프로그래머스 - 커피 심부름

def solution(order):
    answer = 0
    for i in order:
        if "cafelatte" in i:
            answer += 5000
        elif "americano" or "anything" in i:
            answer += 4500
    return answer


print(solution(["cafelatte", "americanoice", "hotcafelatte", "anything"]))
print(solution(["americanoice", "americano", "iceamericano"]))
