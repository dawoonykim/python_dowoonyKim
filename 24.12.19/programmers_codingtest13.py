# 프로그래머스 - 합성수 찾기

def solution(n):
    answer = []
    li = []
    count = 1
    while count <= n:
        
        if n % count == 0:
            li.append(count)
            print(count)
        count += 1
        answer.append(li)

    return answer


print(solution(10))
print(solution(15))
