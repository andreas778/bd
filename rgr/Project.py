from Controller import Controller

class Project(Controller):
    def read(self, where_condition=""):
        if not(where_condition): print(f"Reading a {self.name} records...")
        sql_select = f"SELECT Project_Id, Name, Description, Freelancer_Id, Client_Id FROM {self.name} {where_condition}"
        with self.conn, self.conn.cursor() as cur:
            cur.execute(sql_select)
            for row in cur.fetchall():
                print(f"Project_Id: {row[0]}")
                print(f"Name: {row[1]}")
                print(f"Description: {row[2]}")
                print(f"Freelancer_Id: {row[3]}")
                print(f"Client_Id: {row[4]}")
                print()

    def create(self):
        print(f"Creating a new {self.name} record...")
        while True:
            try:
                project_id = int(input(f"{self.name}_Id: "))
                break
            except:
                print(f"{self.name}_id must be Integer")
        name = input("Name: ")
        description = input("Description: ")        
        while True:
            try:
                freelancer_id = int(input(f"Freelancer_Id: "))
                while True:
                    try:
                        client_id = int(input(f"Client_Id: "))
                        break
                    except:
                        print(f"Client_Id must be Integer")
                break
            except:
                print(f"Freelancer_Id must be Integer")
        sql_insert = f"INSERT INTO {self.name} (Project_Id, Name, Description, Freelancer_Id, Client_Id) VALUES (%s, %s, %s, %s, %s)"
        with self.conn, self.conn.cursor() as cur:
            cur.execute(sql_insert, (project_id, name, description, freelancer_id, client_id))


    def generate(self):
        print(f"Generating random {self.name} records...")
        while True:
            try:
                records_amount = int(input("How many records to generate?"))
                break
            except:
                print("Records amount must be Integer")
        sql_generate = f"INSERT INTO {self.name} (Project_Id, Name, Description, Freelancer_Id, Client_Id)  (select {self.sqlRandomInteger}, {self.sqlRandomString}, {self.sqlRandomString}, {self.sqlRandomInteger}, {self.sqlRandomInteger})"
        for _ in range(records_amount):
            with self.conn, self.conn.cursor() as cur:
                cur.execute(sql_generate)
