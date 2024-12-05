# 프로그래머스 - 가까운 1 찾기

def solution(arr, idx):
    answer = 0
    for i in range(len(arr)):
        if i >= idx and arr[i] == 1:
            answer = i
            break # 위의 조건을 만족하기 때문에 1을 찾고 나서 다시 for문이 돌아가는 것을 막아야 함
        else:
            answer = -1
    return answer


print(solution([0, 0, 0, 1], 1))
print(solution([1, 0, 0, 1, 0, 0], 4))
print(solution([1, 1, 1, 1, 0], 3))
