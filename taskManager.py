# Simple Task Manager that keeps track of tasks to do and puts them in a table
import tkinter
import customtkinter

# System settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

#App Frame
#Size of Window Frame / Window Title etc..
app = customtkinter.CTk() # creates an instance of Custom TKinter
app.geometry("2560x1440")
app.title("Task Manager")

tasklist = []
def startFunction ():
    print("Hello!")
    print("Please enter in your task")
    newTask()
def newTask ():
    taskName = input("Please enter the task name: ", )
    taskDescription = input("What does this task entail? ",)
    taskCompletion = False
    print(taskName)
    print(tasklist)
    print(taskCompletion)
    tasklist.append(taskName, taskDescription, taskCompletion)
def deleteTask(whichElementToDelete):
    tasklist.remove(whichElementToDelete)
    print(tasklist)
    # Deletes task from task list
# Adding UI Elements
# UI Elements are always created with using customtkinter. 
title = customtkinter.CTkLabel(app, text="Task Manager")
title.pack(padx = 15, pady = 15)
createTaskButton = customtkinter.CTkButton(app, width=200,height=150,text="Create Task", command=newTask)
createTaskButton.pack(padx=5, pady=5)
viewTaskButton = customtkinter.CTkButton(app,width=200,height=150, text="View Tasks")
viewTaskButton.pack(padx=5, pady=5)# Run app
deleteTaskDialog = customtkinter.CTkEntry(app, placeholder_text="Which task would you like to delete?", command=deleteTask(whichElementToDelete=input))
deleteTitle = customtkinter.CTkLabel(app, text="Delete Task", text_color="white")
deleteTitle.pack(padx = 100, pady = 100)
deleteTaskDialog.pack(padx = 300, pady = 150)
app.mainloop()