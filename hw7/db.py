import sqlite3

# Connect to SQLite database
connect = sqlite3.connect("schedule.db")
cursor = connect.cursor()

# Create tables if they do not exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY
)
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS schedules (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    task TEXT,
    time TEXT
)
""")
connect.commit()

def add_user(user_id):
    cursor.execute("INSERT OR IGNORE INTO users (user_id) VALUES (?)", (user_id,))
    connect.commit()

def add_task(user_id, task):
    cursor.execute("INSERT INTO schedules (user_id, task) VALUES (?, ?)", (user_id, task))
    connect.commit()

def set_task_time(user_id, time):
    cursor.execute("UPDATE schedules SET time = ? WHERE user_id = ? AND time IS NULL", (time, user_id))
    connect.commit()

def get_schedules(user_id):
    return cursor.execute("SELECT time FROM schedules WHERE user_id = ?", (user_id,)).fetchall()

def delete_task(user_id, time):
    cursor.execute("DELETE FROM schedules WHERE user_id = ? AND time = ?", (user_id, time))
    connect.commit()

def update_task(user_id, old_time, new_time):
    cursor.execute("UPDATE schedules SET time = ? WHERE user_id = ? AND time = ?", (new_time, user_id, old_time))
    connect.commit()
