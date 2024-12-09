class Cal:

    def __init__(self, a, b):
        self.__a = a
        self.__b = b

    def add(self):
        return f"{self.__a} + {self.__b} = {self.__a + self.__b}"

    def sub(self):
        return f"{self.__a} - {self.__b} = {self.__a - self.__b}"

    def mul(self):
        return f"{self.__a} * {self.__b} = {self.__a * self.__b}"

    def div(self):
        if self.__b != 0:
            return f"{self.__a} / {self.__b} = {self.__a / self.__b}"


cal1 = Cal(1, 2)
print(cal1.add())
print(cal1.sub())
print(cal1.mul())
print(cal1.div())
