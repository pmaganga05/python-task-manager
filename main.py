import json
import os

FILE_NAME = "tasks.json"

def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as f:
        return json.load(f)

def save_tasks(tasks):
    with open(FILE_NAME, "w") as f:
        json.dump(tasks, f, indent=4)

def show_tasks(tasks):
    if not tasks:
        print("\nAucune tâche.\n")
        return
    for i, t in enumerate(tasks, 1):
        print(f"{i}. {t}")

def add_task(tasks):
    t = input("Tâche : ")
    tasks.append(t)

def delete_task(tasks):
    show_tasks(tasks)
    try:
        i = int(input("Numéro à supprimer : "))
        tasks.pop(i-1)
    except:
        print("Erreur")

def menu():
    tasks = load_tasks()

    while True:
        print("\n1-Ajouter  2-Voir  3-Supprimer  4-Quitter")
        c = input("> ")

        if c == "1":
            add_task(tasks)
            save_tasks(tasks)
        elif c == "2":
            show_tasks(tasks)
        elif c == "3":
            delete_task(tasks)
            save_tasks(tasks)
        elif c == "4":
            save_tasks(tasks)
            break

if __name__ == "__main__":
    menu()