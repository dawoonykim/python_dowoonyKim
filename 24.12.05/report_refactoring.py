def check_machine():
    print("남은 음료수 : ", vanding_machine)
    # 전역 변수가 적용되는 시점은 프로그램이 동작하고 난 후이기 때문에
    # 전역 변수가 선언된 함수 위에든 아래든 상관없이
    # 동작하는 시점보다 위에 선언만 되어 있으면 끌어다가 사용할 수 있음

def is_drink(drink):
    if drink in vanding_machine:
        return True
    else:
        return False

def add_drink(add_drink_name):
    if is_drink(add_drink_name):
        index = vanding_machine.index(add_drink_name)
        vanding_machine.insert(index, add_drink_name)
    else:
        vanding_machine.append(add_drink_name)

def remove_drink(remove_drink_name):
    if is_drink(remove_drink_name):
        index = vanding_machine.index(remove_drink_name)
        del vanding_machine[index]
    else:
        print("삭제 할 ", remove_drink_name, "가 없습니다.", sep="")

vanding_machine = ["게토레이", "게토레이", "레쓰비", "레쓰비", "생수", "생수", "이프로"]
check_machine()

people = int(input("사용자 종류를 입력하세요 : \n1.소비자\n2.주인\n"))
if not (people == 1 or people == 2):
    print("사용자 종류를 잘못입력했습니다.")
else:
    if people == 1:
        drink = input("마시고 싶은 음료? ")
        if is_drink(drink):
            print(drink, "드릴게요")
            vanding_machine.remove(drink)
        else:
            print(drink, "가 없습니다.", sep="")
    elif people == 2:
        todo = int(input("할 일 선택\n1.추가\n2.삭제\n"))
        if not (todo == 1 or todo == 2):
            print("할 일을 잘못 선택했습니다.")
        else:
            check_machine()
            if todo == 1:
                add_drink_name = input("추가할 음료수? ")
                add_drink(add_drink_name)
            elif todo == 2:
                remove_drink_name = input("삭제할 음료수? ")
                remove_drink(remove_drink_name)

check_machine()
