num = int(input("몇 줄? "))

for i in range(1, num+1):
    line = ""
    for j in range(i):
        line += "*"
    print(line)
print()
for i in range(1, num+1):
    line = ""
    line += " "*(num-i)
    for j in range(i):
        line += "*"
    print(line)
print()
for i in range(1, num+1):
    line=""
    line=" "*(num-i)
    for j in range(i*2-1):
        line+="*"
    print(line)