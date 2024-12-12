name = input("이름 : ")
password = input("비밀번호 : ")
dic = dict()
with open("./member/member.txt", "r") as f:
    for line in f:
        n, p = line.split()
        dic[n] = p

    print(dic)
    if dic[name] == password:
        word = "로그인 성공!!"
    else:
        word = "로그인 실패"

    print(word)
