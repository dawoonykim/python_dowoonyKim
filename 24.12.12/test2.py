name = input("이름 : ")
password = input("비밀번호 : ")

with open("./member/member.txt", "r") as f:
    for line in f:
        n, p = line.split()

        if n == name and p == password:
            word = "로그인 성공!!"
            break
        else:
            word = "로그인 실패"

    print(word)
