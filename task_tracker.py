import json
import os

class TaskManager:
    def __init__(self, filename="tasks.json"):
        self.filename = os.path.join(os.path.expanduser("~"), filename)
        self.tasks = self.load_tasks()

    def load_tasks(self):
        try:
            if os.path.exists(self.filename):
                with open(self.filename, "r") as f:
                    return json.load(f)
        except:
            pass
        return []

    def save_tasks(self):
        try:
            with open(self.filename, "w") as f:
                json.dump(self.tasks, f, indent=4)
        except:
            print("Error: Cannot save file.\n")

    def add_task(self):
        title = input("Enter Title: ")
        description = input("Enter Description: ")

        if not title:
            print("Title cannot be empty!\n")
            return

        self.tasks.append({
            "title": title,
            "description": description
        })

        self.save_tasks()
        print("Task added successfully!\n")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.\n")
            return

        for i, task in enumerate(self.tasks, 1):
            print(f"{i}. {task['title']} - {task['description']}")
        print()

    def delete_task(self):
        self.view_tasks()

        if not self.tasks:
            return

        try:
            num = int(input("Enter task number to delete: "))
            if 1 <= num <= len(self.tasks):
                removed = self.tasks.pop(num - 1)
                self.save_tasks()
                print(f"Deleted: {removed['title']}\n")
            else:
                print("Invalid number!\n")
        except:
            print("Invalid input!\n")

    def run(self):
        print(f"Saving file at: {self.filename}\n")

        while True:
            print("===== Task Tracker =====")
            print("1. Add Task")
            print("2. View Tasks")
            print("3. Delete Task")
            print("4. Exit")

            choice = input("Enter choice: ")

            if choice == "1":
                self.add_task()
            elif choice == "2":
                self.view_tasks()
            elif choice == "3":
                self.delete_task()
            elif choice == "4":
                print("Goodbye!")
                break
            else:
                print("Invalid choice!\n")


if __name__ == "__main__":
    TaskManager().run()