# name = ["1", "2", "3", "2", "2","5","6"]
# a = []
# not_dupl_name = {}
# for i in range(len(name)):
#     if name.count(name[i]) > 1 and name[i] not in a:
#         a.append(name[i])

# set_a = set(a)
# set_name = set(name)
# not_dupl_name = set_name.difference(set_a)
# not_dupl_name = set_name.union(set_a)
# list_name=list(not_dupl_name)
# list_name.sort()
# print(list_name)


name = ["1", "2", "3", "2", "2"]
a = []
dupl_name = []
for i in range(len(name)):
    if name.count(name[i]) > 1 and name[i] not in dupl_name:
        dupl_name.append(name[i])
        print(f"{i}. dupl_name : {dupl_name}")
    elif name[i] not in dupl_name:
        print(f"{i}. name : {name[i]}")
        a.append(name[i])
# print(dupl_name)
print(a)
