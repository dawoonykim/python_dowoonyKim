import os

os.chdir("C:\\Users\\dawoo\\Desktop\\SF7\\python")
dir = os.popen("git status")
print(dir.read())
print(os.listdir())
