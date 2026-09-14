from datetime import datetime, date


class Plan:

    def __init__(self, description, time_range):
        self.date = date.today()
        self.time = datetime.now().strftime("%H:%M:%S")
        self.description = description
        self.time_range = time_range

    def show(self):
        print(f"Date: {self.date}")
        print(f"Time: {self.time}")
        print(f"Description: {self.description}")
        print(f"Time range: {self.time_range}")


def main():

    tasks = []

    while True:

        print("\n===== PLAN =====")
        print("1. Add task")
        print("2. Remove task")
        print("3. Show tasks")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":

            description = input("Enter task: ")
            time_range = input("Enter time range: ")

            task = Plan(description, time_range)
            tasks.append(task)

        elif choice == "2":

            task = input("Enter task to remove: ")

            found = False

            for plan in tasks:
                if plan.description == task:
                    tasks.remove(plan)
                    found = True
                    print("Task removed.")
                    break

            if not found:
                print("Task not found.")

        elif choice == "3":

            print("\n===== TASKS =====")

            if not tasks:
                print("No tasks.")

            else:
                for task in tasks:
                    task.show()

        elif choice == "4":
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()