with open("./member/member.txt", "w") as f:
    f.write("")

print("회원 명부 작성하기기")
n = 1
while n < 4:
    name = input("이름 : ")
    password = input("비밀번호 : ")

    if name != "" and password != "":
        n += 1
        with open("./member/member.txt", "a") as f:
            f.write(f"{name} {password}\n")
    else:
        print("다시 입력하세요.")

with open("./member/member.txt", "r") as f:
    for line in f:
        name, password = line.split()
        print(f"이름 : {name}\t비밀번호 : {password}")
    print(f.read())
