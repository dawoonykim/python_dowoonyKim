# 프로그래머스 - 합성수 찾기

def solution(n):
    answer = []

    for i in range(1, n+1):
        count = 1
        li = []
        while count <= i:
            if i % count == 0:
                li.append(count)
                if len(li) >= 3:
                    if i not in answer:
                        answer.append(i)

            count += 1
        print(f"{i}번째\nli : {li}\nanswer : {answer}")

    return len(answer)


print(solution(10))
print(solution(15))
