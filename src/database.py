import sqlite3

class DatabaseRepository:
    def __init__(self, db_path: str = "database.db"):
        self.connection = sqlite3.connect(db_path)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS Comments (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            message TEXT NOT NULL
            )"""
        )
        self.connection.commit()

    def get_by_id(self, comment_id: int):
        self.cursor.execute(
            """
            SELECT name, message FROM Comments WHERE id = ?""",
            (comment_id,)
        )
        row = self.cursor.fetchone()
        if row is None:
            return None
        return row

    def get_by_name(self, username: str):
        self.cursor.execute(
            """
            SELECT id, message FROM Comments WHERE name = ?""",
            (username,)
        )
        row = self.cursor.fetchone()
        if row is None:
            return None
        return row

    def add(self, comment_id: int, username: str, message: str):
        self.cursor.execute(
            """
            INSERT OR IGNORE INTO Comments (id, name, message) VALUES (?, ?, ?)""",
            (comment_id, username, message)
        )
        self.connection.commit()

    def update(self, comment_id: int, new_message: str):
        self.cursor.execute(
            """
            UPDATE Comments SET message = ? WHERE id = ?""",
            (new_message, comment_id)
        )
        self.connection.commit()

    def delete(self, comment_id: int):
        self.cursor.execute(
            """
            DELETE FROM Comments WHERE id = ?""",
            (comment_id,)
        )
        self.connection.commit()
    
    def close(self):
        try:
            self.cursor.close()
        except Exception:
            pass
        