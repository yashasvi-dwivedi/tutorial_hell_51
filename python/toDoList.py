def toDoList():
    tasks = []

    while True:
        print("\nTo-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

        print("\nOptions:")
        print("1. Add a task")
        print("2. Remove a task")
        print("3. Exit")

        choice = input("Choose an option (1-3): ")

        if choice == "1":
            task = input("Enter the task to add: ")
            tasks.append(task)
            print(f"Task '{task}' added.")
        elif choice == "2":
            if not tasks:
                print("No tasks to remove.")
                continue
            try:
                index = int(input("Enter the task number to remove: ")) - 1
                removed_task = tasks.pop(index)
                print(f"Task '{removed_task}' removed.")
            except (ValueError, IndexError):
                print("Invalid task number.")
        elif choice == "3":
            print("Exiting the To-Do List.")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    toDoList()
