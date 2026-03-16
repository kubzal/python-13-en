class Manager:
    def __init__(self, first_name, last_name, department, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.department = department
        self.salary = salary


class Employee:
    def __init__(self, first_name, last_name, department, position, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.department = department
        self.position = position
        self.salary = salary

    def __str__(self):
        return (
            f"{self.first_name} {self.last_name} - {self.position} ({self.department})"
        )
