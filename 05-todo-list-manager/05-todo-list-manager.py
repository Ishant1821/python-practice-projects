"""
Day 04 (Project 05): Simple To-Do List Manager
A CLI utility demonstrating list manipulation (CRUD operations) in Python.
"""

def main():
    tasks = []

    while True:
        print("\n" + "=" * 35)
        print("📋 TO-DO LIST MANAGER")
        print("=" * 35)
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")
        print("=" * 35)

        choice = input("Select an option (1-4) --> ").strip()
        
        if choice == "1":
            if not tasks:
                print("\n📂 Your to-do list is empty!")
            else:
                print("\n📌 YOUR TASKS:")
                for index, task in enumerate(tasks, start=1):
                    print(f"  {index}. {task}")

        elif choice == "2":
            new_task = input("\nEnter the new task --> ").strip()
            if new_task:
                tasks.append(new_task)
                print(f"✅ Added: '{new_task}'")
            else:
                print("⚠️ Task cannot be empty!")

        elif choice == "3":
            if not tasks:
                print("\n📂 No tasks available to remove.")
            else:
                print("\n📌 YOUR TASKS:")
                for index, task in enumerate(tasks, start=1):
                    print(f"  {index}. {task}")

                try:
                    task_num = int(input("\nEnter task number to remove --> "))
                    if 1 <= task_num <= len(tasks):
                        removed = tasks.pop(task_num - 1)
                        print(f"🗑️ Removed: '{removed}'")
                    else:
                        print("❌ Invalid task number!")
                except ValueError:
                    print("❌ Please enter a valid number.")

        elif choice == "4":
            print("\n👋 Goodbye!")
            break
        else:
            print("❌ Invalid selection! Please choose 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()