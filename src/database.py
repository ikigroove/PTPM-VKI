import sqlite3

class Database:
    def __init__(self, db_path: str = "database.db"):
        self.connection = sqlite3.connect(db_path)
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

    def find_triangle(self, a: float, b: float, c: float):
        self.cursor.execute(
            """
                select triangle_type, err_msg from Triangle where a = ? and b = ? and c = ?
            """,
            (a, b, c)
        )

        row = self.cursor.fetchone()
        if row is None:
            return None
        return row[0], row[1]

    def insert_triangle(self, a: float, b: float, c: float, triangle_type: str, err_msg: str):
        self.cursor.execute(
            """
            insert or ignore into Triangle (a, b, c, triangle_type, err_msg) 
            values (?, ?, ?, ?, ?)
            """,
            (a, b, c, triangle_type, err_msg)
        )
        self.connection.commit()

    def close(self):
        try:
            self.cursor.close()
        except Exception:
            pass
        try:
            self.connection.close()
        except Exception:
            pass