# n = int(input(""))
# m = int(input(""))
# N = []
# M = []
# for i in range(n):
#     N.append(input())
# for i in range(m):
#     M.append(input())
N,M=map(int,input().split())

S = ["baekjoononlinejudge", "startlink",
     "codeplus", "sundaycoding", "codingsh"]

M = ["baekjoon", "codeplus", "codeminus", "startlink", "starlink",
     "sundaycoding", "codingsh", "codinghs", "sondaycoding", "startrink", "icerink"]
setN=set(N)
setM=set(M)

count_N = len(N)
count_M = len(M)
common_elements = N & M
# print(count_N, count_M)
print(len(common_elements))
