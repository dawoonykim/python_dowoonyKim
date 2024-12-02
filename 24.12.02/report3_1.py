vanding_machine = ["게토레이", "게토레이", "레쓰비", "레쓰비", "생수", "생수", "이프로"]
print("남은 음료수 : ", vanding_machine)


people = int(input("사용자 종류를 입력하세요 : \n1.소비자\n2.주인\n"))
if not (people == 1 or people == 2):
    print("사용자 종류를 잘못입력했습니다.")
else:
    if people == 1:
        drink = input("마시고 싶은 음료? ")
        if drink in vanding_machine:
            print(drink, "드릴게요")
            vanding_machine.remove(drink)
        else:
            print(drink, "가 없습니다.", sep="")
    elif people == 2:
        todo = int(input("할 일 선택\n1.추가\n2.삭제\n"))
        if not (todo == 1 or todo == 2):
            print("할 일을 잘못 선택했습니다.")
        else:
            print("남은 음료수 : ", vanding_machine)
            if todo == 1:
                add_drink = input("추가할 음료수? ")
                if add_drink in vanding_machine:
                    index = vanding_machine.index(add_drink)
                    vanding_machine.insert(index, add_drink)
                else:
                    vanding_machine.append(add_drink)
            elif todo == 2:
                remove_drink = input("삭제할 음료수? ")
                if remove_drink in vanding_machine:
                    index = vanding_machine.index(remove_drink)
                    del vanding_machine[index]
                else:
                    print("삭제 할 ", remove_drink, "가 없습니다.", sep="")


print("남은 음료수 : ", vanding_machine)
