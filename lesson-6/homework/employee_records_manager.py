def add_employee():
    with open("employees.txt", "a") as file:
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Employee Name: ")
        position = input("Enter Position: ")
        salary = input("Enter Salary: ")
        file.write(f"{emp_id}, {name}, {position}, {salary}\n")
        print("Employee added successfully!\n")

def view_employees():
    try:
        with open("employees.txt", "r") as file:
            records = file.readlines()
            if not records:
                print("No employee records found.\n")
            else:
                for record in records:
                    print(record.strip())
            print()
    except FileNotFoundError:
        print("No employee records found.\n")

def search_employee():
    emp_id = input("Enter Employee ID to search: ")
    found = False
    try:
        with open("employees.txt", "r") as file:
            for line in file:
                if line.startswith(emp_id + ","):
                    print("Employee Found:", line.strip())
                    found = True
                    break
    except FileNotFoundError:
        pass
    if not found:
        print("Employee not found.\n")

def update_employee():
    emp_id = input("Enter Employee ID to update: ")
    updated_records = []
    found = False
    try:
        with open("employees.txt", "r") as file:
            for line in file:
                if line.startswith(emp_id + ","):
                    name = input("Enter new Employee Name: ")
                    position = input("Enter new Position: ")
                    salary = input("Enter new Salary: ")
                    updated_records.append(f"{emp_id}, {name}, {position}, {salary}\n")
                    found = True
                else:
                    updated_records.append(line)
        with open("employees.txt", "w") as file:
            file.writelines(updated_records)
        if found:
            print("Employee updated successfully!\n")
        else:
            print("Employee not found.\n")
    except FileNotFoundError:
        print("Employee not found.\n")

def delete_employee():
    emp_id = input("Enter Employee ID to delete: ")
    updated_records = []
    found = False
    try:
        with open("employees.txt", "r") as file:
            for line in file:
                if not line.startswith(emp_id + ","):
                    updated_records.append(line)
                else:
                    found = True
        with open("employees.txt", "w") as file:
            file.writelines(updated_records)
        if found:
            print("Employee deleted successfully!\n")
        else:
            print("Employee not found.\n")
    except FileNotFoundError:
        print("Employee not found.\n")

def main():
    while True:
        print("Employee Records Manager")
        print("1. Add new employee record")
        print("2. View all employee records")
        print("3. Search for an employee by Employee ID")
        print("4. Update an employee's information")
        print("5. Delete an employee record")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_employee()
        elif choice == "2":
            view_employees()
        elif choice == "3":
            search_employee()
        elif choice == "4":
            update_employee()
        elif choice == "5":
            delete_employee()
        elif choice == "6":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 6.\n")

main()
