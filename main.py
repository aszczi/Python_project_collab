import datetime
from time import strptime


def addTask(tasks):
    addName = input("Enter name of the task: ")
    addPriority = int(input("Choose the priority for the task: \n 1: UrgentImportant\n 2: NotUrgentImportant \n 3: UrgentNotImportant\n  4: NotUrgentNotImportant"))
    addStatus = int(input("Select task status: \n1: ToDo \n2: InProgress\n 3: Finished"))
    addDeadline = input("Provide a deadline for completing the task (dd-mm-yyyy): ")
    deadlineDate = strptime(addDeadline, "%d.%m.%Y")
    timeLeft = deadlineDate - datetime.datetime.now()
    addCategory = int(input("Select task category: "))
    addDescription = input("Add description: ")

    newTask = {
        "name": addName,
        "priority": addPriority,
        "status": addStatus,
        "deadline": addDeadline,
        "category": addCategory,
        "description": addDescription
    }
    tasks.append(newTask)
    return tasks

def deleteTask(tasks):
    input()

def showTasks(tasks, priority, status, category):

    for task in tasks:
        task["priorityName"] = priority.get(task["priority"], "Unknown")

    for task in tasks:
        task["statusName"] = status.get(task["status"], "Unknown")

    for task in tasks:
        task["categoryName"] = category.get(task["category"], "Unknown")

    for task in tasks:
        task["description"] = task.get(task["description"], "Unknown")
        

    for task in tasks:
        print(f'{task["name"]} - {task["priorityName"]} - {task["statusName"]} - {task["categoryName"]}')

    # desciption =

def menu():
    tasks = []

    priority = {
        1: "UrgentImportant",
        2: "NotUrgentImportant",
        3: "UrgentNotImportant",
        4: "NotUrgentNotImportant",
    }

    status = {
        1: "ToDo",
        2: "InProgress",
        3: "Finished",
    }

    category = {
        1: "Praca",
        2: "Osobiste",
        3: "etc",
    }
    # deadline =
    while True:
        print("----------------------------------------------------")
        print("Wciśnij 0 aby dodać zakończyć.")
        print("Wciśnij 1 aby dodać zadanie.")
        print("Wciśnij 2 aby usunąć zadanie.")
        print("Wciśnij 3 aby edytować zadanie.")
        print("Wciśnij 4 aby oznaczyć zadanie jako zakończone.")
        print("Wciśnij 5 aby wyświetlić informację o zadaniu.")
        print("Wciśnij 6 aby wyświetlić listę zadań ze szczegółami.")
        print("----------------------------------------------------")

        userInput = input()

        match userInput:
            case "0":
                break
            case "1":
                addTask(tasks)
            case "2":
                deleteTask(tasks)
            case "3":
                print("q")
            case "4":
                print("q")
            case "5":
                print("q")
            case "6":
                showTasks(tasks, priority, status, category)
            case _:
                print("Wpisz liczbę od 1 do 6.")

menu()
