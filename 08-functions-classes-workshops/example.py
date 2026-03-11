class Employee:
    def __init__(self, first_name, last_name, department, position, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.department = department
        self.position = position
        self.salary = salary

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.department})"

emp1 = Employee("Jan", "Kowalski", "IT", "Engineer", 20_000)

# print(emp1.first_name)
# print(emp1.salary)

print(emp1)