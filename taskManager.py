# Simple Task Manager that keeps track of tasks to do and puts them in a table
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