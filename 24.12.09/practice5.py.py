class Health:

    def __init__(self, name):
        self.__name = name
        self.__hp = 100

    def set_HP(self, hp):
        hp = max(hp, 0)
        hp = min(hp, 100)

        self.__hp = hp

    def get_HP(self):
        return "HP : "+str(self.__hp)

    def get_name(self):
        return self.__name

    def exercise(self, hours):
        self.set_HP(self.__hp+hours)
        print(f"{hours}시간 운동하다.")

    def drink(self, cups):
        self.set_HP(self.__hp-cups)
        print(f"술을 {cups}잔 마시다.")


p1 = Health("나몸짱")
p1.set_HP(110)
p1.exercise(5)
p1.drink(2)
print(f"{p1.get_name()} - {p1.get_HP()}")
print("="*16)
p2 = Health("나약해")
p2.set_HP(10)
p2.exercise(1)
p2.drink(12)
print(f"{p2.get_name()} - {p2.get_HP()}")
