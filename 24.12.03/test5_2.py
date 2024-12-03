num = int(input("몇 줄? "))

for i in range(num+1):
    for j in range(i):
        print("*", end="")
    print()
print()
for i in range(num+1):
    print(" "*(num-i), end="")
    for j in range(i):
        print("*", end="")
    print()
print()
for i in range(num+1):
    print(" "*(num-i), end="")
    for j in range(i*2-1):
        print("*", end="")
    print()
