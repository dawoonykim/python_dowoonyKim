# 프로그래머스 : 수열과 구간 쿼리4

# 정수 배열 arr와 2차원 정수 배열 queries이 주어집니다.
# queries의 원소는 각각 하나의 query를 나타내며, [s, e, k] 꼴입니다.
# 각 query마다 순서대로 s ≤ i ≤ e인 모든 i에 대해 i가 k의 배수이면 arr[i]에 1을 더합니다.
# 위 규칙에 따라 queries를 처리한 이후의 arr를 return 하는 solution 함수를 완성해 주세요.

def solution(arr, queries):
    answer = arr[:]
    print(answer)
    for i in queries:
        s = i[0]
        e = i[1]
        k = i[2]
        print("(", s, e, k, ")")
        for j in range(len(arr)):
            if s <= j <= e and j % k == 0:
                answer[j] += 1

        print(answer)
    return answer


print(solution([0, 1, 2, 4, 3], [[0, 4, 1], [0, 3, 2], [0, 3, 3]]))
