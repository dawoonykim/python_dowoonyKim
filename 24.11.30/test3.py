a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# even = a[1::2]
odd = a[::2]
# c언어처럼 따로 리스트를 선언을 하고서 그 리스트 안에 값을 넣을 필요가 없음

# print(even)
# for i in range(len(a)):
#     if (a[i] % 2 == 0):
#         even.append(a[i])

# print(even)
# for i in a:
#     if (a[i-1] % 2 == 0):
#         even.append(a[i-1 ])

# print(even)
print(odd)
print(len(a))

for i in range(len(a)):
    print(i)
