N, M = map(int, input().split())
N_S = set()
for i in range(N):
    N_S.add(input())
# S = ["baekjoononlinejudge", "startlink",
#      "codeplus", "sundaycoding", "codingsh"]

M_S = ["baekjoon", "codeplus", "codeminus", "startlink", "starlink",
     "sundaycoding", "codingsh", "codinghs", "sondaycoding", "startrink", "icerink"] # => 중복에 대한 조건이 없으므로

ans = 0

for j in M_S:
    # text = input()
    if j in N_S:
        ans += 1
# setN = set(N)
# setM = set(M)

# count_N = len(N)
# count_M = len(M)
# common_elements = N & M
# print(count_N, count_M)
# print(len(common_elements))

print(ans)
