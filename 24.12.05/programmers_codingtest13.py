# 프로그래머스 - 배열 만들기 3

def solution(arr, intervals):
    answer = []
    
    for i in intervals:
        answer+=arr[i[0]:i[1]+1]
    return answer


print(solution([1, 2, 3, 4, 5],[[1, 3], [0, 4]]	))

