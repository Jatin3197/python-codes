todo_list=[]

while True:
    print("\nTo_Do List Menu:")
    print("1. Add task")
    print("2. View tasks")
    print("3. Mark task as complete")
    print("4. Exit")

    choice= input("Enter a choice from 1 to 4 :")

    if choice=="1":
        task=input("Enter task: ")
        todo_list.append({"task": task,"completed": False})
    
    elif choice=="2":
        if not todo_list:
            print("No tasks in the to-do list.")
        else:
            print("\nTasks:")
            for i, item in enumerate(todo_list, 1):
                status="  " if item["completed"] else " "
                print(f"{i}. [{status}] {item['task']}")

    elif choice==3:
        if not todo_list:
            print("No tasks in the to-do list")
        else:
            task_num= int(input("Enter task number to mark as complete:"))
            if 1 <= task_num <=len(todo_list):
                todo_list[task_num - 1]["completed"]=True
                print("Task marked as completed")
            else:
                print("Invalid task number")
    elif choice==4:
        print("Goodbye!")
        break
    else:
        print("Invalid choice. please try again.")
                
