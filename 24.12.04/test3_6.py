N, M = map(int, input().split())

N_S = set()
M_S = set()

for i in range(N):
    N_S.add(input().strip())
for i in range(M):
    M_S.add(input().strip())

# N_S = ["baekjoononlinejudge", "startlink",
#      "codeplus", "sundaycoding", "codingsh"]

# M_S = ["baekjoon", "codeplus", "codeminus", "startlink", "starlink",
#      "sundaycoding", "codingsh", "codinghs", "sondaycoding", "startrink", "icerink"]

ans = len(N_S & M_S)
print(ans)
A=0
B=0
print(A+B)
print(A-B)
print(A*B)
print(A/B)
print(A%B)