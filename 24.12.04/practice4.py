d = [
    [10, 20],
    [30, 40],
    [50, 60]
]

print(d)
print(d[0][0])
print(d[1][1])

d.append([70, 80])
print(d)

d[0][0] = 90
print(d)

# d[1].pop(1)
# del (d[1][1])
# print(d)

for i in range(len(d)):
    for j in range(len(d[i])):
        print(f"[{i}][{j}] : {d[i][j]}")

for x, y in d: # 구조 분해
    print(x, y)  # => 리스트 길이가 맞지 않으면 에러가 발생함
