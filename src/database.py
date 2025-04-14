import sqlite3
from datetime import datetime

DB_NAME = "tasks.db"

def connect():
    conn = sqlite3.connect(DB_NAME)
    return conn

def create_table():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task TEXT NOT NULL,
            priority TEXT NOT NULL,
            category TEXT NOT NULL,
            due_date TEXT
        )
    ''')
    conn.commit()
    conn.close()

def add_task(task, priority, category, due_date):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO tasks (task, priority, category, due_date)
        VALUES (?, ?, ?, ?)
    ''', (task, priority, category, due_date.strftime("%Y-%m-%d") if due_date else None))
    conn.commit()
    conn.close()

def remove_task(task_id):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
    conn.commit()
    conn.close()

def update_task(task_id, task, priority, category, due_date):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE tasks
        SET task = ?, priority = ?, category = ?, due_date = ?
        WHERE id = ?
    ''', (task, priority, category, due_date.strftime("%Y-%m-%d") if due_date else None, task_id))
    conn.commit()
    conn.close()

def get_all_tasks():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('SELECT id, task, priority, category, due_date FROM tasks')
    rows = cursor.fetchall()
    conn.close()

    tasks = []
    for row in rows:
        due_date = datetime.strptime(row[4], "%Y-%m-%d") if row[4] else None
        tasks.append({
            "id": row[0],
            "task": row[1],
            "priority": row[2],
            "category": row[3],
            "due_date": due_date
        })
    return tasks

def clear_all_tasks():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM tasks')
    conn.commit()
    conn.close()
