# Task: Employee Management Program:
# 1. Create:
#    - Options to add:
#      -> Manager (first name, last name, department, salary)
#      -> Employee (first name, last name, department, position, salary)
# 2. Manage:
#    - Position: display employees at a given position
#    - Subordinates: display employees managed by a selected manager
#    - Balance: display the total salary of all employees and managers
# 3. Exit: the 'exit' option ends the program.

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
        return f"{self.first_name} {self.last_name} - {self.position} ({self.department})"

managers = []
employees = []

def input_managers_data():
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    department = input("Enter department: ")
    salary = float(input("Enter salary: "))

    new_manager = Manager(first_name, last_name, department, salary)
    return new_manager

def input_employee_data():
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    department = input("Enter department: ")
    position = input("Enter position: ")
    salary = float(input("Enter salary: "))

    new_employee = Employee(first_name, last_name, department, position, salary)
    return new_employee

def list_subordinates():
    manager_first_name = input("Enter manager's first name: ")
    manager_last_name = input("Enter manager's last name: ")

    for manager in managers:
        if manager.first_name == manager_first_name and manager.last_name == manager_last_name:
            for employee in employees:
                if employee.department == manager.department:
                    print(employee)

def list_employees_position():
    print("List employees on the position:")

    position = input("Enter position: ")

    for employee in employees:
        if employee.position == position:
            print(employee)

def display_balance():
    total_salary_employees = 0.0
    total_salary_managers = 0.0

    for employee in employees:
        total_salary_employees += employee.salary

    for manager in managers:
        total_salary_managers += manager.salary

    print(f"Salary of all employees: {total_salary_employees} PLN")
    print(f"Salary of all managers: {total_salary_managers} PLN")
    print()
    print(f"Salary of all employees and managers: {total_salary_employees + total_salary_managers} PLN")

while True:
    action = input("What do you want to do? [create, manage, exit]: ").lower()

    if action == "exit":
        break

    elif action == "create":
        while True:
            create_action = input("What do you want to create? [manager, employee, exit]: ").lower()

            if create_action == "exit":
                break

            elif create_action == "manager":
                print("Adding new manager:")

                new_manager = input_managers_data()
                managers.append(new_manager)

            elif create_action == "employee":
                print("Adding new employee:")

                new_employee = input_employee_data()
                employees.append(new_employee)

            else:
                print("Invalid create action")

    elif action == "manage":
        while True:
            manage_action = input("What do you want to manage? [position, subordinates, balance, exit]: ")

            if manage_action == "exit":
                break

            elif manage_action == "position":
                list_employees_position()

            elif manage_action == "subordinates":
                print("List manager's suborinates")

                list_subordinates()

            elif manage_action == "balance":
                print("Balance:")
                display_balance()

            else:
                print("Invalid manage action")


    else:
        print("Invalid action")

print("The end of the program")