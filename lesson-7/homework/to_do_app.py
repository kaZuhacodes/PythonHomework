import json
import csv

class Task:
    def __init__(self, task_id, title, description, due_date, status="Pending"):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

    def to_dict(self):
        return {
            "task_id": self.task_id,
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "status": self.status
        }

    def __str__(self):
        return f"{self.task_id}, {self.title}, {self.description}, {self.due_date}, {self.status}"


class TaskStorage:
    def save_tasks(self, tasks):
        pass

    def load_tasks(self):
        pass


class CSVTaskStorage(TaskStorage):
    FILE_NAME = "tasks.csv"

    def save_tasks(self, tasks):
        with open(self.FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Task ID", "Title", "Description", "Due Date", "Status"])
            for task in tasks:
                writer.writerow([task.task_id, task.title, task.description, task.due_date, task.status])

    def load_tasks(self):
        tasks = []
        try:
            with open(self.FILE_NAME, "r") as file:
                reader = csv.reader(file)
                next(reader)  # Skip header
                for row in reader:
                    tasks.append(Task(*row))
        except FileNotFoundError:
            pass
        return tasks


class JSONTaskStorage(TaskStorage):
    FILE_NAME = "tasks.json"

    def save_tasks(self, tasks):
        with open(self.FILE_NAME, "w") as file:
            json.dump([task.to_dict() for task in tasks], file, indent=4)

    def load_tasks(self):
        tasks = []
        try:
            with open(self.FILE_NAME, "r") as file:
                data = json.load(file)
                for item in data:
                    tasks.append(Task(**item))
        except (FileNotFoundError, json.JSONDecodeError):
            pass
        return tasks


class ToDoApp:
    def __init__(self, storage):
        self.storage = storage
        self.tasks = self.storage.load_tasks()

    def add_task(self):
        task_id = input("Enter Task ID: ").strip()
        if any(task.task_id == task_id for task in self.tasks):
            print("Task ID already exists!")
            return

        title = input("Enter Title: ").strip()
        description = input("Enter Description: ").strip()
        due_date = input("Enter Due Date (YYYY-MM-DD): ").strip()
        status = input("Enter Status (Pending/In Progress/Completed): ").strip()
        self.tasks.append(Task(task_id, title, description, due_date, status))
        print("Task added successfully!\n")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks found.\n")
        else:
            print("\nTasks:")
            for task in self.tasks:
                print(task)
            print()

    def update_task(self):
        task_id = input("Enter Task ID to update: ").strip()
        for task in self.tasks:
            if task.task_id == task_id:
                task.title = input("Enter new Title: ").strip()
                task.description = input("Enter new Description: ").strip()
                task.due_date = input("Enter new Due Date (YYYY-MM-DD): ").strip()
                task.status = input("Enter new Status (Pending/In Progress/Completed): ").strip()
                print("Task updated successfully!\n")
                return
        print("Task not found.\n")

    def delete_task(self):
        task_id = input("Enter Task ID to delete: ").strip()
        self.tasks = [task for task in self.tasks if task.task_id != task_id]
        print("Task deleted successfully!\n")

    def filter_tasks(self):
        status = input("Enter Status to filter by (Pending/In Progress/Completed): ").strip()
        filtered = [task for task in self.tasks if task.status.lower() == status.lower()]
        if not filtered:
            print("No tasks found with that status.\n")
        else:
            print("\nFiltered Tasks:")
            for task in filtered:
                print(task)
            print()

    def save_tasks(self):
        self.storage.save_tasks(self.tasks)
        print("Tasks saved successfully!\n")

    def run(self):
        while True:
            print("Welcome to the To-Do Application!")
            print("1. Add a new task")
            print("2. View all tasks")
            print("3. Update a task")
            print("4. Delete a task")
            print("5. Filter tasks by status")
            print("6. Save tasks")
            print("7. Exit")

            choice = input("Enter your choice: ").strip()
            print()

            if choice == "1":
                self.add_task()
            elif choice == "2":
                self.view_tasks()
            elif choice == "3":
                self.update_task()
            elif choice == "4":
                self.delete_task()
            elif choice == "5":
                self.filter_tasks()
            elif choice == "6":
                self.save_tasks()
            elif choice == "7":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.\n")


# Choose storage format (CSV or JSON)
print("Select Storage Format:")
print("1. CSV")
print("2. JSON")

storage_choice = input("Enter choice: ").strip()
storage = CSVTaskStorage() if storage_choice == "1" else JSONTaskStorage()

# Run the application
app = ToDoApp(storage)
app.run()