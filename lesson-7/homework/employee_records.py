class Employee:
    def __init__(self, employee_id, name, position, salary):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        return f"{self.employee_id}, {self.name}, {self.position}, {self.salary}"


class EmployeeManager:
    FILE_NAME = "employees.txt"

    def add_employee(self):
        employee_id = input("Enter Employee ID: ").strip()
        if self.search_employee(employee_id, silent=True):
            print("Employee ID already exists!")
            return

        name = input("Enter Name: ").strip()
        position = input("Enter Position: ").strip()
        salary = input("Enter Salary: ").strip()

        with open(self.FILE_NAME, "a") as file:
            file.write(f"{employee_id}, {name}, {position}, {salary}\n")
        print("Employee added successfully!\n")

    def view_all_employees(self):
        try:
            with open(self.FILE_NAME, "r") as file:
                employees = file.readlines()
                if not employees:
                    print("No employee records found.")
                else:
                    print("\nEmployee Records:")
                    for employee in employees:
                        print(employee.strip())
                print()
        except FileNotFoundError:
            print("No employee records found.\n")

    def search_employee(self, employee_id, silent=False):
        try:
            with open(self.FILE_NAME, "r") as file:
                for line in file:
                    data = line.strip().split(", ")
                    if data[0] == employee_id:
                        if not silent:
                            print("Employee Found:\n" + line.strip() + "\n")
                        return data
        except FileNotFoundError:
            if not silent:
                print("No employee records found.\n")
        if not silent:
            print("Employee not found.\n")
        return None

    def update_employee(self):
        employee_id = input("Enter Employee ID to update: ").strip()
        records = []
        updated = False

        try:
            with open(self.FILE_NAME, "r") as file:
                records = file.readlines()

            with open(self.FILE_NAME, "w") as file:
                for line in records:
                    data = line.strip().split(", ")
                    if data[0] == employee_id:
                        name = input("Enter new Name: ").strip()
                        position = input("Enter new Position: ").strip()
                        salary = input("Enter new Salary: ").strip()
                        file.write(f"{employee_id}, {name}, {position}, {salary}\n")
                        updated = True
                    else:
                        file.write(line)

            print("Employee updated successfully!\n" if updated else "Employee not found.\n")
        except FileNotFoundError:
            print("No employee records found.\n")

    def delete_employee(self):
        employee_id = input("Enter Employee ID to delete: ").strip()
        records = []
        deleted = False

        try:
            with open(self.FILE_NAME, "r") as file:
                records = file.readlines()

            with open(self.FILE_NAME, "w") as file:
                for line in records:
                    data = line.strip().split(", ")
                    if data[0] != employee_id:
                        file.write(line)
                    else:
                        deleted = True

            print("Employee deleted successfully!\n" if deleted else "Employee not found.\n")
        except FileNotFoundError:
            print("No employee records found.\n")

    def run(self):
        while True:
            print("Welcome to the Employee Records Manager!")
            print("1. Add new employee record")
            print("2. View all employee records")
            print("3. Search for an employee by Employee ID")
            print("4. Update an employee's information")
            print("5. Delete an employee record")
            print("6. Exit")

            choice = input("Enter your choice: ").strip()
            print()

            if choice == "1":
                self.add_employee()
            elif choice == "2":
                self.view_all_employees()
            elif choice == "3":
                emp_id = input("Enter Employee ID to search: ").strip()
                self.search_employee(emp_id)
            elif choice == "4":
                self.update_employee()
            elif choice == "5":
                self.delete_employee()
            elif choice == "6":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.\n")


# Run the program
manager = EmployeeManager()
manager.run()