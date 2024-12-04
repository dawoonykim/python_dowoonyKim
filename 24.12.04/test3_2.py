# n = int(input(""))
# m = int(input(""))
# N = []
# M = []
# for i in range(n):
#     N.append(input())
# for i in range(m):
#     M.append(input())
N, M = map(int, input().split())
S = set()
for i in range(N):
    S.add(input())
# S = ["baekjoononlinejudge", "startlink",
#      "codeplus", "sundaycoding", "codingsh"]

# M = ["baekjoon", "codeplus", "codeminus", "startlink", "starlink",
#      "sundaycoding", "codingsh", "codinghs", "sondaycoding", "startrink", "icerink"]

ans = 0

for j in range(M):
    text = input()
    if text in S:
        ans += 1
# setN = set(N)
# setM = set(M)

# count_N = len(N)
# count_M = len(M)
# common_elements = N & M
# print(count_N, count_M)
# print(len(common_elements))

print(ans)
