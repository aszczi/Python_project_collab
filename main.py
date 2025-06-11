from datetime import datetime
import os
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator


def saveTasks(tasks):
    with open('tasks.txt', 'w') as file:
        for task in tasks:
            line = f"{task['name']}|{task['priority']}|{task['status']}|{task['deadline']}|{task['category']}|{task['description']}\n"
            file.write(line)

def loadTasks():
    tasks = []
    if os.path.exists('tasks.txt'):
        with open('tasks.txt', 'r') as file:
            for line in file:
                if line.strip(): 
                    task_data = line.strip().split('|')
                    task = {
                        "name": task_data[0],
                        "priority": int(task_data[1]),
                        "status": int(task_data[2]),
                        "deadline": task_data[3],
                        "category": int(task_data[4]),
                        "description": task_data[5],
                    }
                    tasks.append(task)
    return tasks

def addTask(tasks):
    addName = input("Podaj nazwę zadania: ")
    while True:
        try:
            addPriority = int(input("Podaj priorytet zadania: \n 1: Ważne i Pilne \n 2: Ważne i niepilne \n 3: Pilne, nie tak ważne\n 4: Nie tak ważne i niepilne\n"))
            if addPriority in [1, 2, 3, 4]:
                break
            else:
                print("Podaj liczbę od 1 do 4.")
        except ValueError:
            print("Niepoprawny priorytet. Spróbuj ponownie, wpisz liczbę od 1 do 4:")
    while True:
        try:
            addStatus = int(input("Podaj status zadania: \n 1: Do zrobienia \n 2: W trakcie\n 3: Ukończone\n"))
            if addStatus in [1, 2, 3]:
                break
            else:
                print("Podaj liczbę od 1 do 3.")
        except ValueError:
            print("Niepoprawny status. Spróbuj ponownie, wpisz liczbę od 1 do 3:")


    if addStatus != 3:
        while True:
            addDeadline = input("Podaj termin wykonania zadania (dd.mm.yyyy): ")
            try:
                deadlineDate = datetime.strptime(addDeadline, "%d.%m.%Y")
                timeLeft = deadlineDate - datetime.now()
                break
            except ValueError:
                print("Niepoprawny format daty. Spróbuj ponownie, (dd.mm.yyyy):")
    else:
        deadlineDate = datetime.now()
        addDeadline = deadlineDate.strftime("%d.%m.%Y")
        timeLeft = 0

    while True:
        try:
            addCategory = int(input("Podaj kategorię zadania: \n 1: Praca\n 2: Osobiste\n 3: etc\n"))
            if addCategory in [1, 2, 3]:
                break
            else:
                print("Podaj liczbę od 1 do 3.")
        except ValueError:
            print("Niepoprawna kategoria. Spróbuj ponownie, wpisz liczbę od 1 do 3:")

    addDescription = input("Podaj opis zadania: ")

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
    if not tasks:
        print("Brak zadań do usunięcia.")
        return tasks

    print("\nLista zadań:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task['name']}")

    try:
        task_num = int(input("\nPodaj numer zadania do usunięcia: ")) - 1
        if 0 <= task_num < len(tasks):
            del tasks[task_num]
            saveTasks(tasks)
            print("Zadanie zostało usunięte.")
        else:
            print("Nieprawidłowy numer zadania.")
    except ValueError:
        print("Proszę podać numer.")

    return tasks

def editTask(tasks, priority, status, category):
    if not tasks:
        print("Brak zadań do edycji.")
        return tasks

    print("\nLista zadań:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task['name']}")

    try:
        taskNum = int(input("\nPodaj numer zadania do edycji: ")) - 1
        if not (0 <= taskNum < len(tasks)):
            print("Nieprawidłowy numer zadania.")
            return tasks

        task = tasks[taskNum]

        print("\nEdycja zadania:")
        print("1. Nazwa")
        print("2. Priorytet")
        print("3. Status")
        print("4. Termin")
        print("5. Kategoria")
        print("6. Opis")
        print("0. Anuluj")

        choice = input("Wybierz co chcesz edytować (0-6): ")

        if choice == "1":
            task['name'] = input("Nowa nazwa: ")

        elif choice == "2":
            print("\nWybierz nowy priorytet:")
            for key, value in priority.items():
                print(f"{key}: {value}")
            newPriority = int(input("Nowy priorytet: "))
            if newPriority in priority:
                task['priority'] = newPriority
            else:
                print("Nieprawidłowy priorytet. Edycja anulowana.")

        elif choice == "3":
            print("\nWybierz nowy status:")
            for key, value in status.items():
                print(f"{key}: {value}")
            newStatus = int(input("Nowy status: "))
            if newStatus in status:
                task['status'] = newStatus
            else:
                print("Nieprawidłowy status. Edycja anulowana.")

        elif choice == "4":
            newDeadline = input("Nowy termin (dd.mm.yyyy): ")
            try:
                datetime.datetime.strptime(newDeadline, "%d.%m.%Y")
                task['deadline'] = newDeadline
            except ValueError:
                print("Nieprawidłowy format daty. Edycja terminu anulowana.")

        elif choice == "5":
            print("\nWybierz nową kategorię:")
            for key, value in category.items():
                print(f"{key}: {value}")
            newCategory = int(input("Nowa kategoria: "))
            if newCategory in category:
                task['category'] = newCategory
            else:
                print("Nieprawidłowa kategoria. Edycja anulowana.")

        elif choice == "6":
            task['description'] = input("Nowy opis: ")

        elif choice == "0":
            print("Anulowano edycję.")
            return tasks

        else:
            print("Nieprawidłowy wybór. Edycja anulowana.")
            return tasks

        saveTasks(tasks)
        print("Zadanie zostało zaktualizowane.")

    except ValueError:
        print("Proszę podać poprawny numer.")

    return tasks

def markDone(tasks, priority, status, category):
    if not tasks:
        print("Brak zadań do oznaczenia jako zakończone.")
        return tasks

    print("\nLista zadań:")
    for i, task in enumerate(tasks, 1):
        status_symbol = "✓" if task['status'] == 3 else ""
        print(f"{i}. {task['name']} {status_symbol} (Status: {status.get(task['status'], 'Unknown')}, Termin: {task['deadline']})")

    try:
        taskNum = int(input("\nPodaj numer zadania do oznaczenia jako zakończone: ")) - 1
        if not (0 <= taskNum < len(tasks)):
            print("Nieprawidłowy numer zadania.")
            return tasks

        if tasks[taskNum]['status'] == 3:
            print("To zadanie jest oznaczone jako zakończone.")
        else:
            tasks[taskNum]['status'] = 3
            saveTasks(tasks)
            print(f"Zadanie \"{tasks[taskNum]['name']}\" zostało oznaczone jako zakończone.")

    except ValueError:
        print("Proszę podać poprawny numer.")

    return tasks

def taskInfo(tasks, priority, status, category):
    if not tasks:
        print("Brak zadań do sprawdzenia.")
        return tasks

    print("\nO którym zadaniu chcesz wyświetlić pełne informacje:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task['name']} (Status: {status.get(task['status'], 'Unknown')}, Termin: {task['deadline']})")

    try:
        taskNum = int(input("\nPodaj numer zadania do wyświetlenia informacji: ")) - 1
        if not (0 <= taskNum < len(tasks)):
            print("Nieprawidłowy numer zadania.")
            return tasks

        task = tasks[taskNum]

        print("----------------------------------------------------")
        print(f"Nazwa: {task['name']}")
        print(f"Opis: {task['description']}")
        print(f"Priorytet: {priority.get(task['priority'], 'Unknown')}")
        print(f"Status: {status.get(task['status'], 'Unknown')}")
        print(f"Kategoria: {category.get(task['category'], 'Unknown')}")
        print(f"Termin wykonania: {task['deadline']}")

    except ValueError:
        print("Proszę podać poprawny numer.")

    return tasks

def showTasks(tasks, priority, status, category):
    print("\nLista zadań:")
    for i, task in enumerate(tasks, 1):
        status_symbol = "✓" if task['status'] == 3 else ""
        print(f"{i}. {task['name']} {status_symbol} (Status: {status.get(task['status'], 'Unknown')}, Termin: {task['deadline']})")

def plot_counts(tasks, key, mapping, title):
    counts = {}
    for t in tasks:
        k = t[key]
        counts[k] = counts.get(k, 0) + 1

    labels = [mapping[k] for k in sorted(counts)]
    values = [counts[k] for k in sorted(counts)]

    fig, ax = plt.subplots()
    ax.bar(labels, values)
    ax.set_title(title)
    ax.set_ylabel('Liczba zadań')
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))  
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_status(tasks, status):
    plot_counts(tasks, 'status', status, 'Zadania według stanu')

def plot_priority(tasks, priority):
    plot_counts(tasks, 'priority', priority, 'Zadania według priorytetu')

def plot_category(tasks, category):
    plot_counts(tasks, 'category', category, 'Zadania według kategorii')


def menu():
    tasks = loadTasks()

    priority = {
        1: "Ważne i Pilne",
        2: "Ważne i niepilne",
        3: "Pilne, nie tak ważne",
        4: "Nie tak ważne i niepilne",
    }

    status = {
        1: "Do zrobienia",
        2: "W trakcie",
        3: "Ukończone",
    }

    category = {
        1: "Praca",
        2: "Osobiste",
        3: "etc",
    }

    while True:
        print("----------------------------------------------------")
        print("Wciśnij 0 aby zakończyć działanie aplikacji.")
        print("Wciśnij 1 aby dodać zadanie.")
        print("Wciśnij 2 aby usunąć zadanie.")
        print("Wciśnij 3 aby edytować zadanie.")
        print("Wciśnij 4 aby oznaczyć zadanie jako zakończone.")
        print("Wciśnij 5 aby wyświetlić informację o zadaniu.")
        print("Wciśnij 6 aby wyświetlić listę zadań ze szczegółami.")
        print("Wciśnij 7 aby wyświetlić wykresy dotyczące zadań.")
        print("----------------------------------------------------")

        userInput = input()

        match userInput:
            case "0":
                print("Zapisywanie zadań i zamykanie programu...")
                saveTasks(tasks)
                break
            case "1":
                tasks = addTask(tasks)
            case "2":
                tasks = deleteTask(tasks)
            case "3":
                tasks = editTask(tasks, priority, status, category)
            case "4":
                tasks = markDone(tasks, priority, status, category)
            case "5":
                taskInfo(tasks, priority, status, category)
            case "6":
                showTasks(tasks, priority, status, category)
            case "7":
                plot_status(tasks, status)
                plot_priority(tasks, priority)
                plot_category(tasks, category)
            case _:
                print("Wpisz liczbę od 1 do 7.")

if __name__ == "__main__":
    menu()
