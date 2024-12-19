# 프로그래머스 - 캐릭터의 좌표

def solution(keyinput, board):

    un, dn = (board[1]//2), -(board[1]//2)
    ln, rn = -(board[0]//2), (board[0]//2)

    # print(f"un : {un}, dn : {dn}, ln : {ln}, rn : {rn}")

    center = [0, 0]
    # print(center)
    for key in keyinput:
        if key is "left" and center[0] > ln:
            center[0] -= 1
        elif key is "right" and center[0] < rn:
            center[0] += 1
        elif key is "up" and center[1] < un:
            center[1] += 1
        elif key is "down" and center[1] > dn:
            center[1] -= 1

    return center


print(solution(["left", "right", "up", "right", "right"], [11, 11]))
print(solution(["down", "down", "down", "down", "down"], [7, 9]))
