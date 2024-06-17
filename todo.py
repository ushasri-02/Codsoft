todo = []
def add(task):
    todo.append(task)
def delete(ind):
    if 0 <= ind < len(todo):
        del todo[ind]
    else:
        print("Invalid index.")
def mark(ind):
    if 0 <= ind < len(todo):
        todo[ind] += " [Completed]"
    else:
        print("Invalid index.")
def update(ind, new_task):
    if 0 <= ind < len(todo):
        todo[ind] = new_task
    else:
        print("Invalid index.")
def display():
    if todo==[]:
        print("No tasks to display.")
    else:
        print("Tasks:")
        for ind, task in enumerate(todo, start=1):
            print(f"{ind}. {task}")
def main():
    while True:
        print("\nMenu:")
        print("1. Add Task")
        print("2. Display Task")
        print("3. Mark Task as Completed")
        print("4. Delete Tasks")
        print("5. Update Task")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter the task: ")
            add(task)
        elif choice == "2":
            display()
        elif choice == "3":
            ind = int(input("Enter the index of the task to mark as completed: ")) - 1
            mark(ind)
        elif choice == "4":
            ind = int(input("Enter the index of the task to delete: ")) - 1
            delete(ind)
        elif choice == "5":
            ind = int(input("Enter the index of the task to update: ")) - 1
            new_task = input("Enter the new task: ")
            update(ind, new_task)
        elif choice == "6":
            print("Have a nice day..")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
