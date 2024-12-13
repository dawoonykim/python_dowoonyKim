with open("./output/data.bin", "wb") as f:
    txt = "안녕"
    f.write(txt.encode())  # 압축

with open("./output/data.bin", "rb") as f:
    data = f.read()
    print(data)
    print(data.decode())  # 압축 해제

