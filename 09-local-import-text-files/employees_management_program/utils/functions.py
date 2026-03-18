from models import Employee, Manager


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


def list_subordinates(managers, employees):
    manager_first_name = input("Enter manager's first name: ")
    manager_last_name = input("Enter manager's last name: ")

    for manager in managers:
        if (
            manager.first_name == manager_first_name
            and manager.last_name == manager_last_name
        ):
            for employee in employees:
                if employee.department == manager.department:
                    print(employee)


def list_employees_position(employees):
    print("List employees on the position:")

    position = input("Enter position: ")

    for employee in employees:
        if employee.position == position:
            print(employee)


def display_balance(employees, managers):
    total_salary_employees = 0.0
    total_salary_managers = 0.0

    for employee in employees:
        total_salary_employees += employee.salary

    for manager in managers:
        total_salary_managers += manager.salary

    print(f"Salary of all employees: {total_salary_employees} PLN")
    print(f"Salary of all managers: {total_salary_managers} PLN")
    print()
    print(
        f"Salary of all employees and managers: {total_salary_employees + total_salary_managers} PLN"
    )
