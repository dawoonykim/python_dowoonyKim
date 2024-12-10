class Calculator:
    def __init__(self):
        self.value = 100

    def sub(self, value):
        self.value -= value


class MinLimitCalculator(Calculator):
    def sub(self, value):
        # self.value=max(0,self.value-value)
        super().sub(value)
        self.value = max(0, self.value)

    # def sub(self):
    #     self.value -= 10

    # def sub(self, value1, value2):
    #     self.value = value1-value2

    def sub(self, *args):
        self.value = args[0]


cal = MinLimitCalculator()
cal.sub(20)
cal.sub(90)
print(cal.value)
