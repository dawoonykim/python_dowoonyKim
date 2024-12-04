# 백준 오븐 시계

h, m = map(int, input().split())
cooking_time = int(input())
m = m+cooking_time
if m >= 60:
    h = h + 1*(m//60)
    if h >= 24:
        h %= 24
    m = m - 60*(m//60)
print(h, m)
