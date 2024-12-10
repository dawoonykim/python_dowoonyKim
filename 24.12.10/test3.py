import random

set_list = set()

while len(set_list) < 6:
    num = random.randint(1, 45)
    set_list.add(num)

li = list(set_list)
li.sort()
print(li)

# => set은 sort()각 안되므로 sorted()를 하면 됨
print(sorted(set_list))
