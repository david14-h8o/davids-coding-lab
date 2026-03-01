# Simple To-Do List in Python

todo_list = []

def show_menu():
    print("\nTo-Do List Menu")
    print("1. Add task")
    print("2. View tasks")
    print("3. Remove task")
    print("4. Quit")

while True:
    show_menu()
    choice = input("Choose an option: ")

    if choice == "1":
        task = input("Enter a new task: ")
        todo_list.append(task)
        print(f"Task '{task}' added.")
    elif choice == "2":
        if not todo_list:
            print("No tasks yet!")
        else:
            print("\nYour tasks:")
            for i, task in enumerate(todo_list, start=1):
                print(f"{i}. {task}")
    elif choice == "3":
        if not todo_list:
            print("No tasks to remove.")
        else:
            for i, task in enumerate(todo_list, start=1):
                print(f"{i}. {task}")
            index = int(input("Enter task number to remove: "))
            if 1 <= index <= len(todo_list):
                removed = todo_list.pop(index - 1)
                print(f"Task '{removed}' removed.")
            else:
                print("Invalid number.")
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, try again.")