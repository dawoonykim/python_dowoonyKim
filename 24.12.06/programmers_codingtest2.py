# 프로그래머스 - 배열 조각하기

def solution(arr, query):
    answer = arr
    count=0
    for i in query:
        if count % 2 == 0:
            answer = answer[:i+1]
            # 변수에 다시 저장하지 않으면 초기화한 값이 반환됨
        else:
            answer = answer[i:]
        count+=1

    return answer


print(solution([0, 1, 2, 3, 4, 5], [4, 1, 2]))
