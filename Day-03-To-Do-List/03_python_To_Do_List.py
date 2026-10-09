#To Do List

Task = []

while True:
  print("##TO DO LIST##")
  print("1. Add Tasks")
  print("2. View tasks")
  print("3. Delete tasks")
  print("4. EXIT")
  
  Choice = int(input("Enter Your Choice: "))
#Add Task  
  if Choice == 1 :
               task = input("Enter your task: ") 
               Task.append(task)
               print("Task Added Successfully!")
#View task
  elif Choice == 2 :
    if len(Task) == 0:
         print("No Tasks")
    else :
         print("/nYour Tasks: ")
    for i , task in enumerate(Task, start=1):
        print(f"{i}. {task}")
#Delete task
  elif Choice == 3 :
    if len(Task) == 0:
        print("No Tasks")
    else :
        print("/nYour Tasks: ")
        for i , task in enumerate(Task, start=1):
            print(f"{i}. {task}")
        task_number = int(input("Enter the task Number you want to delete: "))
        if 1 <= task_number <= len (Task) :
            Task.pop(task_number - 1)
        else :
            print("Invalid Task Number")
#Exit
  elif Choice == 4 : 
    print("Exiting the TO DO LIST")
    break

  else :
    print("Invalid choice. Please try again")
