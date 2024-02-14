class TaskManager:
    def __init__(self):
        self.tasks = []

    def run(self):
        print("Welcome to Personal Task Manager!")
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")
            self.process_choice(choice)

    def display_menu(self):
        print("\nMenu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Exit")

    def process_choice(self, choice):
        if choice == "1":
            self.add_task()
        elif choice == "2":
            self.view_tasks()
        elif choice == "3":
            self.mark_completed()
        elif choice == "4":
            print("Thank you for using Personal Task Manager!")
            exit()
        else:
            print("Invalid choice. Please try again.")

    def add_task(self):
        title = input("Enter task title: ")
        description = input("Enter task description: ")
        priority = input("Enter task priority (High/Medium/Low): ").capitalize()
        self.tasks.append({"title": title, "description": description, "priority": priority, "completed": False})
        print("Task added successfully!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks found.")
            return
        print("\nTasks:")
        for index, task in enumerate(self.tasks, start=1):
            status = "Completed" if task["completed"] else "Pending"
            print(f"{index}. {task['title']} - Priority: {task['priority']} - Status: {status}")

    def mark_completed(self):
        self.view_tasks()
        task_index = int(input("Enter the index of the task to mark as completed: ")) - 1
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]["completed"] = True
            print("Task marked as completed!")
        else:
            print("Invalid task index.")

if __name__ == "__main__":
    task_manager = TaskManager()
    task_manager.run()