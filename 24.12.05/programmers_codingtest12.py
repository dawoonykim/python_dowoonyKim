# 프로그래머스 - 첫 번째로 나오는 음수

def solution(num_list):

    for i in num_list:
        if i < 0:
            index = num_list.index(i)
            return index
    return -1


print(solution([12, 4, 15, 46, 38, -2, 15]))
print(solution([13, 22, 53, 24, 15, 6]))
