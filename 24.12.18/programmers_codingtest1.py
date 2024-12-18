# 프로그래머스 - 안전지대


def solution(board):
    answer = 0
    n = len(board)
    print(f"n : {n}")
    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]
    boom = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 1:
                boom.append((i, j))
    # print(boom)

    for x, y in boom:
        for i in range(8):
            nx = x+dx[i]
            ny = y+dy[i]
            print(f"nx : {nx} ny : {ny}")

            if 0 <= nx < n and 0 <= ny < n:
                board[nx][ny] = 1
    for i in board:
        answer += i.count(0)
    return answer


print(solution([[0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0]]))
# print(solution([[0, 0, 0, 0, 0],
#                 [0, 0, 0, 0, 0],
#                 [0, 0, 0, 0, 0],
#                 [0, 0, 1, 1, 0],
#                 [0, 0, 0, 0, 0]]))
# print(solution([[1, 1, 1, 1, 1, 1],
#                 [1, 1, 1, 1, 1, 1],
#                 [1, 1, 1, 1, 1, 1],
#                 [1, 1, 1, 1, 1, 1],
#                 [1, 1, 1, 1, 1, 1],
#                 [1, 1, 1, 1, 1, 1]]))
