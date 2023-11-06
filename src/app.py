import Todo


def run():
    todo = Todo.Todo()
    while True:
        print("1. Add task")
        print("2. Remove task")
        print("3. Display tasks")
        print("4. Exit")

        raw_choice = input("Enter your choice: ")

        if type(raw_choice) != int:
            print("Invalid choice. Try again.")
            continue

        choice = int(raw_choice)

        if choice == 1:
            task = input("Enter task: ")
            todo.add(task)
        elif choice == 2:
            task = input("Enter task: ")
            todo.remove(task)
        elif choice == 3:
            todo.display()
        elif choice == 4:
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    run()
