a = [3, 4, 2, 1]
a.sort(reverse=True)
print(a)

b = ["a", "c", "b", "d"]
b.sort()
print(b)

c = ["1", "10", "2", "11"]  # 문자는 사전 순서로 정렬
c.sort()
print(c)

d = ["강남", "강북", "서", "asdf", "서", "서"]
# d.sort()
print(d)

print(d.index("서"))
first = d.index("서")+1
print(first+d[first:].index("서"))

print(d.count("서"))
