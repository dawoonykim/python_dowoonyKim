# N, M = map(int, input().split())
# N_S = set()
# for i in range(N):
#     N_S.add(input())
N_S = ["baekjoononlinejudge", "startlink",
     "codeplus", "sundaycoding", "codingsh"]

M_S = ["baekjoon", "codeplus", "codeminus", "startlink", "starlink",
     "sundaycoding", "codingsh", "codinghs", "sondaycoding", "startrink", "icerink"]

ans = 0
for i in N_S:
    for j in M_S:
    # text = input()
        if i in j:
            ans += 1
# setN = set(N)
# setM = set(M)

# count_N = len(N)
# count_M = len(M)
# common_elements = N & M
# print(count_N, count_M)
# print(len(common_elements))

print(ans)
