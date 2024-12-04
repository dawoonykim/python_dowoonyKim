# 백준 오븐 시계

h, m = map(int, input().split())
cooking_time = int(input())


if m+cooking_time >= 60:
    if m >= 120:
        h += 1*(m//60)
        m -= 60*(m//60)
        # if h == 24:
        #     h = 0
    else:
        h += 1
        m -= 60
if h == 24:
    h = 0
print(h, m)
