N, M = map(int, input().split())
N_S = list()
for i in range(N):
    N_S.append(input())
# N_S = ["baekjoononlinejudge", "startlink",
#      "codeplus", "sundaycoding", "codingsh"]

# M_S = ["baekjoon", "codeplus", "codeminus", "startlink", "starlink",
#      "sundaycoding", "codingsh", "codinghs", "sondaycoding", "startrink", "icerink"]

ans = 0
for _ in range(M):
    text = input()
    if text in N_S:
        ans += 1
# setN = set(N)
# setM = set(M)

# count_N = len(N)
# count_M = len(M)
# common_elements = N & M
# print(count_N, count_M)
# print(len(common_elements))

print(ans)
