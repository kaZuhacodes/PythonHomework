import json
import csv

# Load tasks from JSON
def load_tasks(filename="tasks.json"):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Save tasks to JSON
def save_tasks(tasks, filename="tasks.json"):
    with open(filename, "w") as file:
        json.dump(tasks, file, indent=4)

# Display tasks
def display_tasks(tasks):
    print("\nTasks:")
    print("ID | Task Name       | Completed | Priority")
    print("-" * 40)
    for task in tasks:
        print(f"{task['id']:2} | {task['task']:15} | {task['completed']} | {task['priority']}")

# Modify task completion
def mark_task_completed(tasks, task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            print(f"\nTask '{task['task']}' marked as completed!")
            return
    print("Task not found!")

# Calculate statistics
def task_statistics(tasks):
    total_tasks = len(tasks)
    completed_tasks = sum(1 for task in tasks if task["completed"])
    pending_tasks = total_tasks - completed_tasks
    avg_priority = sum(task["priority"] for task in tasks) / total_tasks if total_tasks > 0 else 0

    print("\nTask Statistics:")
    print(f"Total tasks: {total_tasks}")
    print(f"Completed tasks: {completed_tasks}")
    print(f"Pending tasks: {pending_tasks}")
    print(f"Average priority: {avg_priority:.2f}")

# Convert JSON to CSV
def convert_to_csv(tasks, filename="tasks.csv"):
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Task", "Completed", "Priority"])
        for task in tasks:
            writer.writerow([task["id"], task["task"], task["completed"], task["priority"]])
    print(f"\nTasks saved to {filename} successfully!")

# Main Execution
if __name__ == "__main__":
    tasks = load_tasks()
    
    while True:
        print("\n1. View Tasks")
        print("2. Mark Task as Completed")
        print("3. View Statistics")
        print("4. Convert to CSV")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            task_id = int(input("Enter Task ID to mark as completed: "))
            mark_task_completed(tasks, task_id)
            save_tasks(tasks)  # Save changes
        elif choice == "3":
            task_statistics(tasks)
        elif choice == "4":
            convert_to_csv(tasks)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice, try again!")