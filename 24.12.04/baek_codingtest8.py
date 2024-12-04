# 백준 알람시계

h, m = map(int, input().split())

if h == 0 and m-45 < 0:
    h = 23
    m = 60+m-45
elif m-45 < 0:
    h -= 1
    m = 60+m-45
else:
    m = m-45

print(h, m)
