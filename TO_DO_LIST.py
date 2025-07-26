import os
import json
task_list = []
def load():
    global task_list
    if os.path.exists("todo_data.json"):
        with open("todo_data.json", "r") as f:
            task_list = json.load(f)
    else:
        task_list = []

def save():
    with open("todo_data.json", "w") as f:
        json.dump(task_list, f, indent=2)

def show_tasks():
    if len(task_list) == 0:
        print("No tasks to show.")
    else:
        print("Your To-Do List:")
        for idx, item in enumerate(task_list):
            status = "Done" if item["done"] else "Pending"
            print(f"{idx + 1}. {item['task']} - {status}")

def add_task():
    t = input("Enter task: ")
    task_list.append({"task": t, "done": False})
    print("Task added.")

def update_task():
    show_tasks()
    try:
        num = int(input("Enter task number to edit: ")) - 1
        if 0 <= num < len(task_list):
            new_text = input("Enter updated task: ")
            task_list[num]["task"] = new_text
            print("Task updated.")
        else:
            print("Invalid number.")
    except:
        print("Invalid input.")

def mark_done():
    show_tasks()
    try:
        num = int(input("Enter number to mark as done: ")) - 1
        if 0 <= num < len(task_list):
            task_list[num]["done"] = True
            print("Marked as done.")
        else:
            print("Invalid number.")
    except:
        print("Error: please enter a number.")

def delete_task():
    show_tasks()
    try:
        num = int(input("Enter number to delete: ")) - 1
        if 0 <= num < len(task_list):
            removed = task_list.pop(num)
            print(f"Deleted: {removed['task']}")
        else:
            print("Invalid task number.")
    except:
        print("Error: enter a number.")

def show_menu():
    print("\n--- TO-DO MENU ---")
    print("1. Show Tasks")
    print("2. Add Task")
    print("3. Update Task")
    print("4. Mark Task as Done")
    print("5. Delete Task")
    print("6. Save and Exit")


load()
while True:
    show_menu()
    option = input("Choose (1-6): ")

    if option == "1":
        show_tasks()
    elif option == "2":
        add_task()
    elif option == "3":
        update_task()
    elif option == "4":
        mark_done()
    elif option == "5":
        delete_task()
    elif option == "6":
        save()
        print("Saved. Exiting...")
        break
    else:
        print("Invalid choice.")
