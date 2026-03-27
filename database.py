import sqlite3

conn = sqlite3.connect("documents.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS docs (
    id INTEGER PRIMARY KEY,
    name TEXT,
    content TEXT
)
""")

def save_doc(name, content):
    cursor.execute("INSERT INTO docs (name, content) VALUES (?, ?)", (name, content))
    conn.commit()

def get_docs():
    cursor.execute("SELECT name, content FROM docs")
    return cursor.fetchall()