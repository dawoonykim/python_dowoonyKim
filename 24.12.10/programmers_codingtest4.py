# 프로그래머스 - 정사각형으로 만들기

def solution(arr):

    rows = len(arr)
    cols = max(len(row) for row in arr) if arr else 0


    square_size = max(rows, cols)
    print(f"rows : {rows}, cols : {cols}, square_size : {square_size}")
    answer = [[0]*square_size for _ in range(square_size)]

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            answer[i][j] = arr[i][j]

    return answer


print(solution([[572, 22, 37],
                [287, 726, 384],
                [85, 137, 292],
                [487, 13, 876]]))
print(solution([[57, 192, 534, 2],
                [9, 345, 192, 999]]))
print(solution([[1, 2],
                [3, 4]]))
