import sqlite3

class Database:
    def __init__(self):
        self.connection = sqlite3.connect('database.db')
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute(
            """
            create table if not exists Triangle (
                a real not null, 
                b real not null, 
                c real not null, 
                triangle_type text, 
                err_msg text,
                primary key (a, b, c)
            )
            """
        )
        self.connection.commit()

    def insert_triangle(self, a: float, b: float, c: float, triangle_type: str, err_msg: str):
        self.cursor.execute(
            """
            insert into Triangle (a, b, c, triangle_type, err_msg) 
            values (?, ?, ?, ?, ?)
            """,
            (a, b, c, triangle_type, err_msg)
        )
        self.connection.commit()

