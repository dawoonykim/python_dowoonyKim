def hello():
    global count
    if count == 3:
        return # 리턴하는 것이 가장 깔끔한 코드
    print("Hello, World!")
    count += 1
    hello()
    
count = 0
hello()
