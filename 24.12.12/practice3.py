with open("./output/input.txt", "a", encoding="utf8") as f:
    while True:
        text = input("저장할 내용 입력(종료-z)")
        if text == "z" or text == "Z":
            break
            # sys.exit()
        f.write(text+"\n")
