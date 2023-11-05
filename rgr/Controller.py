import psycopg2
from time import perf_counter

class Controller:
    sqlRandomString = "chr(trunc(65 + random()* 50)::int) || chr(trunc(65 + random() * 25)::int) || chr(trunc(65 +random() * 25)::int) || chr(trunc(65 + random() * 25)::int)"
    sqlRandomInteger = "trunc(random()*1000)::int"

    def __init__(self, connection_string, name):
        self.connection_string = connection_string
        self.conn = psycopg2.connect(connection_string)
        self.name = name

    def read(self, where_condition=""):
        pass

    def create(self):
        pass

    def update(self):
        print(f"Updating {self.name} records...")
        while True:
            try:
                field_to_find = input("Enter the name of the option you want to find with: ")
                value_to_find = input("Enter the value to find: ")
                self.read(f"WHERE {field_to_find} = '{value_to_find}'")
                break
            except Exception as e:
                print(e)

        while True:
            try:
                field_to_update = input("Enter the name of the option you want to change: ")
                value_to_set = input("Enter the new value: ")
                sql_update = f"UPDATE {self.name} SET {field_to_update} = %s WHERE {field_to_find} = %s"
                with self.conn, self.conn.cursor() as cur:
                    cur.execute(sql_update, (value_to_set, value_to_find))
                break
            except Exception as e:
                print(e)
        print("Records updated successfully")

    def delete(self):
        print(f"Deleting a {self.name} record...")
        while True:
            try:
                id = int(input(f"Enter {self.name}_Id: "))
                break
            except:
                print("{self.name}_Id must be Integer")
        sql_delete = f"DELETE FROM {self.name} WHERE {self.name}_Id = %s"
        with self.conn, self.conn.cursor() as cur:
            cur.execute(sql_delete, (id,))
        print("Records deleted successfully")

    def generate(self):
        pass

    def find(self):
        print(f"Finding a {self.name} records...")
        sql_find = f"WHERE "
        x = 0
        while True:
            try:
                while True:
                    option = input("Enter the name of the option you want to find with: ")
                    value = input("Enter value: ")
                    x = input("If you want to add another option to find with, enter 1: ")
                    if x == '1':
                        sql_find += f"{option} ='{value}' AND "
                    else:
                        sql_find += f"{option} ='{value}'"
                        break
                t1 = perf_counter() 
                self.read(sql_find)
                t2 = perf_counter()
                print("Records found successfully, elapsed time in ms:", t2-t1)
                break      
            except Exception as e:
                print(e)


