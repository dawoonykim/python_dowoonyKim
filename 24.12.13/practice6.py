class Animal:
    def breath(self):
        print("숨을 쉰다")

    def cry(self):
        raise NotImplementedError


class Dog(Animal):
    def sleep(self):
        print("강아지가 잠을 잔다")

    def cry(self):
        print("멍~ 멍~")


d = Dog()
d.breath()
d.sleep()
d.cry()