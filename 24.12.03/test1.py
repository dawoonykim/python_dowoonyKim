i = 0
flag = True
while flag:

    i += 1
    if i == 10:
        flag = False

    if i % 2 != 1:
        continue
    print(i)
    # 이 위치에 코드가 놓이게 되면, i==10일 때
    # continue 코드 때문에 "if i == 10" 부분이 실행되지 않음
    # 따라서 같은 코드라도 적절한 위치에 존재하는 것이 중요함
    # if i == 10:
    #     flag = False
print("끝")
