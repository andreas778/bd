from Freelancer import Freelancer
from Project import Project
from Task import Task
from Client import Client


def main():
    connection_string = "dbname=postgres user=postgres password=4455 host=localhost"
    table = 0
    action = 0

    while True:
        table = first_menu()
        if table == 0:
            return
        controller = None

        if table == 1:
            name = "Freelancer"
            action = second_menu(name)
            controller = Freelancer(connection_string, name)
        elif table == 2:
            name = "Project"
            action = second_menu(name)
            controller = Project(connection_string, name)
        elif table == 3:
            name = "Task"
            action = second_menu(name)
            controller = Task(connection_string, name)
        elif table == 4:
            name = "Client"
            action = second_menu(name)
            controller = Client(connection_string, name)

        if action == 1:
            controller.read()
        elif action == 2:
            controller.create()
        elif action == 3:
            controller.update()
        elif action == 4:
            controller.delete()
        elif action == 5:
            controller.generate()
        elif action == 6:
            controller.find()

def first_menu():
    while True:
        print("Choose the table to edit:")
        print("1. Freelancer")
        print("2. Project")
        print("3. Task")
        print("4. Client")
        choice = input()
        try:
            choice = int(choice)
            if 0 < choice < 5:
                return choice
        except ValueError:
            pass

def second_menu(table_to_change):
    while True:
        print(f"Choose what you want to do with the '{table_to_change}' table:")
        print("1. Read")
        print("2. Create")
        print("3. Update")
        print("4. Delete")
        print("5. Generate")
        print("6. Find")
        choice = input()
        try:
            choice = int(choice)
            if 0 < choice < 7:
                return choice
        except ValueError:
            pass

if __name__ == "__main__":
    main()

