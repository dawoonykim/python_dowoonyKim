def solution(arr):
    stk = []
    i = 0

    while len(arr) > i:
        if not stk:
            stk.append(arr[i])
            i += 1
        elif stk and stk[-1] < arr[i]:
            stk.append(arr[i])
            i += 1
        elif stk and stk[-1] > arr[i]:
            stk.pop()

    return stk


print(solution([1, 4, 2, 5, 3]))
