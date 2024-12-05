# 프로그래머스 - 리스트 자르기

def solution(n, slicer, num_list):
    answer = []
    a = slicer[0]
    b = slicer[1]
    c = slicer[2]

    if n == 1:
        return num_list[:b+1]
    elif n == 2:
        return num_list[a:]
    elif n == 3:
        return num_list[a:b+1]
    elif n == 4:
        return num_list[a:b+1:c]


print(solution(3, [1, 5, 2], [1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(solution(4, [1, 5, 2], [1, 2, 3, 4, 5, 6, 7, 8, 9]))
