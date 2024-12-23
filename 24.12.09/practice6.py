class Employee:
    serial_num = 100
    
    def __init__(self, name):
        Employee.serial_num += 1
        self.id = Employee.serial_num
        self.name = name

    def __str__(self):
        return f"사번 : {self.id}, 이름 : {self.name}"

e1 = Employee("최사원")
print(e1)

e2 = Employee("안사원")
print(e2)

e3 = Employee("한사원")
print(e3)

employee = [
    Employee("구름"),
    Employee("별"),
    Employee("행성"),
    Employee("달")
]

for i in employee:
    print(i)
