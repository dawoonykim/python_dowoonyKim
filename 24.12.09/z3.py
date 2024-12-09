class Employee:
    serial_num = 1000

    def __init__(self, name):
        Employee.serial_num += 1
        self.__name = name
        self.__id = Employee.serial_num

    def __str__(self):
        return f"사번 : {self.__id}, 이름 : {self.__name}"


e1 = Employee("최사원")
e2 = Employee("안사원")
e3 = Employee("한사원")
print(e1)
print(e2)
print(e3)

employee = [
    Employee("구름"),
    Employee("별"),
    Employee("행성"),
    Employee("달")
]

for i in employee:
    print(i)

print("\n".join(map(str, employee)))
