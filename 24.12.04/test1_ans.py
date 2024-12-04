name = ["1", "2", "3", "2", "2"]
a = []
dupl_name = []
for i in range(len(name)):
    if a.count(name[i]) < 1:
        a.append(name[i])
# print(dupl_name)
print(a)