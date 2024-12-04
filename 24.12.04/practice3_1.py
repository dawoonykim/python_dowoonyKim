a = {}
print(type(a))  # <class 'dict'>

b = {1}
print(type(b))  # <class 'set'>\

c = dict()
c = {1: "a", "b": "b"}
print(c)

# key and value 추가
c[2] = "c"
c["c"] = 2
print(c)


# key로 삭제
del c[2]
del c["b"]
print(c)

# print(c[2])
print(c.get(2))

print(c.keys())
print(list(c.keys()))

print(c.values())

for i in c.keys():
  print(i, c[i])