num = int(input("몇 초....? "))

list = []

for i in range(1, num+1):
    list.append(i)

list.reverse()

for i in list:
    print(i, end=" ")
print("발사!")
