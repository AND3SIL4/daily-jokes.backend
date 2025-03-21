import sqlite3
from datetime import datetime

DATABASE = "app/db/jokes.db"  # path of the folder and file with data


def init():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS jokes(id INTEGER PRIMARY KEY,content TEXT NOT NULL,date DATE NULL,score INTEGER DEFAULT 0)"
    )
    conn.commit()
    conn.close()


class Database:
    def __init__(self, db_file=DATABASE):
        self.db_file = db_file

    def connect(self):
        return sqlite3.connect(self.db_file)

    def get_joke_by_date(self, date):
        conn = self.connect()
        cursor = conn.cursor()
        # Validate if the joke already exists and return it
        cursor.execute(
            "SELECT id, content, score FROM jokes WHERE date = ? LIMIT 1", (date,)
        )
        daily_joke = cursor.fetchone()
        if daily_joke:
            conn.close()
            return {
                "id": daily_joke[0],
                "content": daily_joke[1],
                "score": daily_joke[2],
            }
        else:
            cursor.execute(
                "UPDATE jokes SET date = ? WHERE id = (SELECT id FROM jokes ORDER BY RANDOM() LIMIT 1)",
                (date,),
            )
            conn.commit()
            cursor.execute(
                "SELECT id, content, score FROM jokes WHERE date = ? LIMIT 1", (date,)
            )
            daily_joke = cursor.fetchone()
            conn.close()
            if daily_joke:
                return {
                    "id": daily_joke[0],
                    "content": daily_joke[1],
                    "score": daily_joke[2],
                }
            return None

    def add_joke(self, joke_data):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO jokes (content) VALUES (?)", (joke_data.content,))
        conn.commit()
        conn.close()

    def rate_joke(self, joke_id, score):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("UPDATE jokes SET score = ? WHERE id = ?", (score, joke_id))
        updated = cursor.rowcount
        conn.commit()
        conn.close()
        return updated > 0


init()
