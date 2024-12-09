class Person:
    def __init__(self):
        self._name = ""  # 멤버 변수 초기화
        self._age = 0

    def set_name(self, name):
        self._name = name

    def set_age(self, age):
        self._age = age

    def get_name(self):
        return self._name

    def get_age(self):
        return self._age


p1 = Person()
p1.set_name("흥부")
p1.set_age(35)
print(f"이름 : {p1.get_name()}, 나이 : {p1.get_age()}")


p2 = Person()
p2.set_name("놀부")
p2.set_age(38)
print(f"이름 : {p2.get_name()}, 나이 : {p2.get_age()}")
