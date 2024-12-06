# 프로그래머스 - 2의 영역

def solution(arr):
    answer = []
    index_list = []
    for i in range(len(arr)):
        if arr[i] == 2:
            index_list.append(i)
    # print(index_list)
    start = index_list[0]
    end = index_list[-1]
    print(f"start : {start} end : {end}")

    return answer


print(solution([1, 2, 1, 4, 5, 2, 9]))
print(solution([1, 2, 1]))
print(solution([1, 1, 1]))
print(solution([1, 2, 1, 2, 1, 10, 2, 1]))
