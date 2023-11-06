class Todo:
    def __init__(self) -> None:
        self.todoList = []

    def add(self, todo):
        self.todoList.append(todo)
        print("Task added:", todo)

    def remove(self, todo):
        if todo in self.todoList:
            self.todoList.remove(todo)
            print("Task removed:", todo)
        else:
            print("Task not found in the to-do list.")

    def display(self):
        if len(self.todoList) == 0:
            print("Your to-do list is empty.")
        else:
            print("To-Do List:")
            for i, todo in enumerate(self.todoList, start=1):
                print(f"{i}. {todo}")
