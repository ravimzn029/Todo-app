---

# 📝 Task Management App (To-Do CLI)

This is a simple **Command-Line To-Do List Application** built in Python for beginners. It allows users to **add**, **update**, **delete**, and **view tasks** interactively through the terminal.

---

## 🚀 Features

* 📌 Add tasks
* ✏️ Update existing tasks
* ❌ Delete tasks
* 👀 View current task list
* 🔚 Exit the program

---

## 🧑‍💻 How It Works

1. The program first asks how many tasks you want to add initially.
2. You enter each task one by one.
3. Then, you can choose from the menu:

   * `1` to add a new task
   * `2` to update an existing task
   * `3` to delete a task
   * `4` to view all tasks
   * `5` to exit the program

---

## 📦 Requirements

* Python 3.x
  *(No third-party libraries needed)*

---

## ▶️ How to Run

1. Save the code in a file, e.g., `todo.py`.
2. Open your terminal or command prompt.
3. Run the script using:

   ```bash
   python todo.py
   ```

---

## 🛠 Sample Code

```python
def task():
    tasks = []
    print("____Welcome to the task management app_____")

    total_task = int(input("Enter how many tasks you want to add = "))
    for i in range(1, total_task + 1):
        task_name = input(f"Enter the task {i} = ")
        tasks.append(task_name)
    print(f"Today's tasks are: \n{tasks}")    

    while True:
        operation = int(input("Enter\n 1-Add\n 2-Update\n 3-Delete\n 4-View\n 5-Stop\n= "))
        
        if operation == 1:
            add = input("Enter the task you want to add = ")
            tasks.append(add)
            print(f"Task '{add}' has been successfully added.")
        
        elif operation == 2:
            update = input("Enter the task you want to update = ")
            if update in tasks:
                updated = input("Enter the new task = ")
                ind = tasks.index(update)
                tasks[ind] = updated
                print(f"Updated task to '{updated}' successfully.")
            else:
                print("Task not found.")
        
        elif operation == 3:
            delete = input("Enter the task you want to delete = ")
            if delete in tasks:
                tasks.remove(delete)
                print(f"Task '{delete}' has been deleted.")
            else:
                print("Task not found.")
        
        elif operation == 4:
            print(f"Current Tasks: {tasks}")
        
        elif operation == 5:
            print("Closing the program.")
            break
        
        else:
            print("Invalid input.")
```

---

## ✅ Ideal For

* Python beginners
* CLI tool practice
* Understanding lists and loops
* Basic CRUD operations in Python

---

## 📬 Feedback

If you found this helpful or have suggestions for improvement, feel free to share!

---

