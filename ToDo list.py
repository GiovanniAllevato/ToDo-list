import json
import os

FILE_NAME = "todo.json"

def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    return []

def save_task(tasks):
    with open(FILE_NAME, "w") as f:
        json.dump(tasks, f, indent=4)
        
def show_tasks(tasks):
    if not tasks:
        print("\n✅ Nessun task nella lista.")
        return
    print("\n📋 Lista ToDo:")
    for i, task in enumerate(tasks, start=1):
        status = "✔" if task["done"] else "❌"
        print(f"{i}. [{status}] {task['title']}")
        
def add_task(tasks):
    title = input("Inserisci il nuovo task: ")
    tasks.append({"title": title, "done": False})
    print(f"➕ Task '{title}' aggiunto!")
    
def complete_task(tasks):
    show_tasks(tasks)
    try:
        num = int(input("Numero del task completato: "))
        tasks[num-1]["done"] = True
        print(f"✔ Task '{tasks[num-1]['title']}' completato!")
    except (ValueError, IndexError):
        print("⚠ Numero non valido.")
        
def delete_task(tasks):
    show_tasks(tasks)
    try:
        num = int(input("Numero del task da eliminare: "))
        removed = tasks.pop(num-1)
        print(f"🗑 Task '{removed['title']}' eliminato!")
    except (ValueError, IndexError):
        print("⚠ Numero non valido.")
        
def main():
    tasks = load_tasks()
    
    while True:
        print("\n--- MENU ---")
        print("1. Mostra lista")
        print("2. Aggiungi task")
        print("3. Completa task")
        print("4. Elimina task")
        print("5. Esci")
        
        choice = input("Scegli un opzione: ")
        
        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            save_task(tasks)
            print("💾 Lista salvata. Uscita...")
            break
        else:
            print("⚠ Opzione non valida.")
            
if __name__ == "__main__":
    main()