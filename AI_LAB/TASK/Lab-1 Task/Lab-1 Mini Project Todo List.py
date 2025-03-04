# -----Todo List-----

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"Task" : task, "Completed" : False})
        print(f"Task {task} Added to the List...") 

    def remove_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            removed_task = self.tasks.pop(task_index)
            print(f'Task "{removed_task["Task"]}" removed from the List....') 
        else:
            print("Invalid! Task Index....")

    def complete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]["Completed"] = True
            print(f'Task "{self.tasks[task_index]["Task"]}" marked as Completed!')
        else:
            print("Invalid! Task Index.")

    def view_task(self):
        if not self.tasks:
            print("No Task In The List!!!!")
            return
        for index, task in enumerate(self.tasks):
            status = "[O]" if task["Completed"] else "[X]"
            print(f"{index}. {status} {task['Task']}.")


def main():
    todo_list = TodoList()

    while True:
        print("\n-------Todo List-------")
        print("\n----Todo List Menu:----")
        print() 
        print("1.Add Task")
        print("2.Remove Task")
        print("3.Complete Task")
        print("4.View Task")
        print("5.Exit")

        choice = input("Enter a choice (1-5) :") 

        if choice == '1':
            task = input("Enter a Task to Add:")
            todo_list.add_task(task)
        elif choice == '2':
            task_index = int(input("Enter the task index to Remove:"))
            todo_list.remove_task(task_index)
        elif choice == '3':
            task_index = int(input("Enter task index to complete:"))
            todo_list.complete_task(task_index)
        elif choice == '4':
            todo_list.view_task()
        elif choice == '5':
            print("Exiting.........")
            break
        else:
            print("Enter a valid choice!") 

main()                               