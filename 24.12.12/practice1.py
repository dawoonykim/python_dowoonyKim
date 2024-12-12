# f1 = open("text.txt", "w")
# f1.write("Hello World\n")
# input("멈춰")
# f1.close()

# f2 = open("text.txt", "a")
# f2.write("new Hello World\n")
# f2.close()

# f3 = open("text.txt", "w")
# f3.write("Hello World222\n\nBye\n")
# f3.close()

f3 = open("text.txt", "w")
f3.write("12345678\n")
f3.close()

f4 = open("text.txt", "r+")
print(f4.read())
print(f4.tell())
f4.seek(4)
print(f4.write("8"))
# print(f4.readlines())
f4.close()

f5 = open("text.txt", "r+")
str5 = f5.read()
print(f5.tell())
f5.seek(str5.find("6"))
print(f5.write("1"))
# print(f4.readlines())
f4.close()


with open("text.txt", "r+") as f6:
    str6 = f6.read()
    print(f6.tell())
    f6.seek(str6.find("4"))
    print(f6.write("3"))
