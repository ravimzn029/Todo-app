def task():
    tasks = []
    print("____Welcome to he task management app_____")

    total_task = int(input("Enter how many task you want to add = "))
    for i in range(1, total_task + 1):
        task_name = input(f"Enter the task {i} = ")
        tasks.append(task_name)
    print(f"today task is \n {tasks}")    

    while True:
      operation = int(input("Enter\n 1-Add\n 2-update\n 3-Delete\n 4-view\n 5-Stop\n = "))
      if operation == 1:
        add = input("Enter the task you want to add = ")
        tasks.append(add)
        print(f"Task {add} has been successfully ......")

      elif operation == 2:
        update = input("Enter the name you want to update = ")
        if update in tasks:
            updated = input("Enter the new task you want to update = ")
            ind = tasks.index(update)
            tasks[ind] = updated
            print(f"Updated task {updated} succesfully.....")
        else:
          print("invalid input")    
      elif operation == 3:
        delete = input("Enter the name you want to delete = ")
        if delete in tasks:
          idx = tasks.index(delete)
          del tasks[idx]
          print(f"task {delete} has been successfully deleted")
        else:
            print("invalid input")
      elif operation == 4:
        print(f"Total Task = {tasks}")

      elif operation == 5:
        print("Closing the program")
        break

      else:
        print("Invalid input")  
task()