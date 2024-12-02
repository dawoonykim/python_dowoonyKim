vanding_machine = ["게토레이", "레쓰비", "생수", "이프로"]

print("============RESTART")
drink = input("마시고 싶은 음료? ")

if drink in vanding_machine:
    print(drink, "드릴게요.")
else:
    print(drink, "는 지금 없네요.", sep="")
