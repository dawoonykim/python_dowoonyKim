a = [1, 2, 3, 4, 5]
b = []
c = []
d = []

for i in a:
    b.append(i*3)

print(f"b = {b}")

c = [i*3 for i in a]
print(f"c = {c}")

d = [i*3 for i in a if i % 2 == 0]
print(f"d = {d}")
