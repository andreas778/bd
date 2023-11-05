from Controller import Controller

class Task(Controller):
    def read(self, where_condition=""):
        if not(where_condition): print(f"Reading a {self.name} records...")
        sql_select = f"SELECT Task_Id, Description, State, Project_Id FROM {self.name} {where_condition}"
        with self.conn, self.conn.cursor() as cur:
            cur.execute(sql_select)
            for row in cur.fetchall():
                print(f"Task_Id: {row[0]}")
                print(f"Name: {row[1]}")
                print(f"State: {row[2]}")
                print(f"Project_Id: {row[3]}")
                print()

    def create(self):
        print(f"Creating a new {self.name} record...")
        while True:
            try:
                project_id = int(input(f"{self.name}_Id: "))
                break
            except:
                print(f"{self.name}_id must be Integer")
        description = input("Description: ")        
        state = input("State: ")
        while True:
            try:
                freelancer_id = int(input(f"Project_Id: "))
                break
            except:
                print(f"Project_Id must be Integer")
        sql_insert = f"INSERT INTO {self.name} (Task_Id, Description, State, Project_Id) VALUES (%s, %s, %s, %s, %s)"
        with self.conn, self.conn.cursor() as cur:
            cur.execute(sql_insert, (task_id, description, state, project_id))


    def generate(self):
        print(f"Generating random {self.name} records...")
        while True:
            try:
                records_amount = int(input("How many records to generate?"))
                break
            except:
                print("Records amount must be Integer")
        sql_generate = f"INSERT INTO {self.name} (Task_Id, Description, State, Project_Id)  (select {self.sqlRandomInteger}, {self.sqlRandomString}, {self.sqlRandomString}, {self.sqlRandomInteger})"
        for _ in range(records_amount):
            with self.conn, self.conn.cursor() as cur:
                cur.execute(sql_generate)
