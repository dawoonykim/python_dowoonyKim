class Calculate:
    def __init__(self, a, b):
        self.__a = a
        self.__b = b

    def add(self):
        print(self.__a+self.__b)

    def sub(self):
        print(self.__a-self.__b)

    def mul(self):
        print(self.__a*self.__b)

    def div(self):
        if self.__b != 0:
            print(self.__a/self.__b)
        else:
            print("division Error")

cal1 = Calculate(4, 1)
cal1.add()
cal1.sub()
cal1.mul()
cal1.div()
