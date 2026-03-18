from utils.functions import (
    input_managers_data,
    input_employee_data,
    list_subordinates,
    list_employees_position,
    display_balance,
)

managers = []
employees = []

while True:
    action = input("What do you want to do? [create, manage, exit]: ").lower()

    if action == "exit":
        break

    elif action == "create":
        while True:
            create_action = input(
                "What do you want to create? [manager, employee, exit]: "
            ).lower()

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
            manage_action = input(
                "What do you want to manage? [position, subordinates, balance, exit]: "
            )

            if manage_action == "exit":
                break

            elif manage_action == "position":
                list_employees_position(employees)

            elif manage_action == "subordinates":
                print("List manager's suborinates")

                list_subordinates(managers, employees)

            elif manage_action == "balance":
                print("Balance:")
                display_balance(employees, managers)

            else:
                print("Invalid manage action")

    else:
        print("Invalid action")

print("The end of the program")
