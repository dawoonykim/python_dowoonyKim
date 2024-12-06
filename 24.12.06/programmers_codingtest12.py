# 프로그래머스 - 수열과 구간 쿼리

def solution(arr, queries):
    answer = arr
    for i in range(len(queries)):
        s = queries[i][0]
        e = queries[i][1]
        
        for i in range(s,e+1):
            answer[i]+=1

    return answer


print(solution([0, 1, 2, 3, 4], [[0, 1], [1, 2], [2, 3]]))
