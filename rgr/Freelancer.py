from Controller import Controller

class Freelancer(Controller):
    def read(self, where_condition=""):
        if not(where_condition): print(f"Reading a {self.name} records...")
        sql_select = f"SELECT Freelancer_Id, Name, Specialization FROM {self.name} {where_condition}"
        with self.conn, self.conn.cursor() as cur:
            cur.execute(sql_select)
            for row in cur.fetchall():
                print(f"Freelancer_Id: {row[0]}")
                print(f"Name: {row[1]}")
                print(f"Specialization: {row[2]}")
                print()

    def create(self):
        print(f"Creating a new {self.name} record...")
        while True:
            try:
                freelancer_id = int(input(f"{self.name}_Id: "))
                break
            except:
                print(f"{self.name}_id must be Integer")
        name = input("Name: ")
        specialization = input("Specialization: ")
        sql_insert = f"INSERT INTO {self.name} (Freelancer_Id, Name, Specialization) VALUES (%s, %s, %s)"
        with self.conn, self.conn.cursor() as cur:
            cur.execute(sql_insert, (freelancer_id, name, specialization))


    def generate(self):
        print(f"Generating random {self.name} records...")
        while True:
            try:
                records_amount = int(input("How many records to generate?"))
                break
            except:
                print("Records amount must be Integer")
        sql_generate = f"INSERT INTO {self.name} (Freelancer_Id, Name, Specialization)  (select {self.sqlRandomInteger}, {self.sqlRandomString}, {self.sqlRandomString})"
        for _ in range(records_amount):
            with self.conn, self.conn.cursor() as cur:
                cur.execute(sql_generate)

