# 백준 주사위 세개
from collections import Counter
n1, n2, n3 = map(int, input().split())
answer = 0
counter = Counter([n1, n2, n3])

if len(counter) == 1:
    answer = 10000+n1*1000
elif 2 in counter.values() and 1 in counter.values():
    multiple = [k for k, v in counter.items() if v == 2]
    single = [k for k, v in counter.items() if v == 1]
    answer = 1000+multiple[0]*100
else:
    bigger = max([n1, n2, n3])
    answer = bigger*100

print(answer)