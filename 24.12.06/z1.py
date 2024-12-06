def hello():
    global count
    if count == 3:
        return
    print("hello")
    count += 1
    hello()


count = 0
hello()
