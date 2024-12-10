class Supermarket:

    count = 0

    def __init__(self, location, name, product, customer):
        self.__location = location
        self.__name = name
        self.__product = product
        self.__customer = customer
        Supermarket.count += 1

    def print_location(self):
        print(f"location : {self.__location}")

    def change_category(self, product):
        self.__product = product

    def show_list(self):
        print(F"current product : {self.__product}")

    def enter_customer(self):
        self.__customer += 1

    def show_info(self):
        print(f"location : {self.__location}, product : {
              self.__product}, customer : {self.__customer}")

    def show_supermarket_count(self):
        print(f"Supermarket count : {Supermarket.count}")


a = Supermarket("마포", "이마트", "생활용품", 3)
a.print_location()
a.show_info()
a.change_category("가전제품")
a.show_info()
a.enter_customer()
a.show_info()
a.show_supermarket_count()

b = Supermarket("신촌", "이마트", "세제", 1)
b.print_location()
b.show_info()
b.change_category("가전제품")
b.show_info()
b.enter_customer()