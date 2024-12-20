# 프로그래머스 - 2차원으로 만들기기

def solution(num_list, n):
    answer = []
    li = []
    for i in range(1,len(num_list)+1):
        li.append(num_list[i-1])
        if i % n == 0:
            answer.append(li)
            li = []
    
    return answer


print(solution([1, 2, 3, 4, 5, 6, 7, 8], 2))
print(solution([100, 95, 2, 4, 5, 6, 18, 33, 948], 3))
