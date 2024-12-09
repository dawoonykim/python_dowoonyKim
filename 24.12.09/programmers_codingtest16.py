# 프로그래머스 - 배열의 원소 삭제

def solution(arr, delete_list):
    answer = []
    for i in range(len(delete_list)):
        if delete_list[i] in arr:
            idx = arr.index(delete_list[i])
            del arr[idx]
    answer = arr
    return answer


print(solution([293, 1000, 395, 678, 94], [94, 777, 104, 1000, 1, 12]))
print(solution([110, 66, 439, 785, 1], [377, 823, 119, 43]))
