class Country:
    def __init__(self):
        self.name = "나라이름"
        self.population = "인구 수"
        self.capital = "수도"

    def show(self):
        print("국가 클래스의 메서드")


class Korea(Country):
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"국가 이름은 : {self.name}")


Country = Korea("대한민국")
Country.show()
print(Country.name)
Country.show_name()
