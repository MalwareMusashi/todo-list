# Initialize an empty to-do list
todo_list = []

# Function to add a task to the to-do list
def add_task(task):
    todo_list.append(task)
    print("Task added:", task)

# Function to remove a task from the to-do list
def remove_task(task):
    if task in todo_list:
        todo_list.remove(task)
        print("Task removed:", task)
    else:
        print("Task not found in the to-do list.")

# Function to display the to-do list
def display_list():
    if len(todo_list) == 0:
        print("Your to-do list is empty.")
    else:
        print("To-Do List:")
        for i, task in enumerate(todo_list, start=1):
            print(f"{i}. {task}")

# Main program loop
while True:
    print("\nOptions:")
    print("1. Add a task")
    print("2. Remove a task")
    print("3. Display to-do list")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if choice == '1':
        task = input("Enter the task you want to add: ")
        add_task(task)
    elif choice == '2':
        task = input("Enter the task you want to remove: ")
        remove_task(task)
    elif choice == '3':
        display_list()
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")
