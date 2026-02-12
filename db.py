import sqlite3
import os
from datetime import datetime

# Crea il database e la tabella se non esistono
def init_db():
    conn = sqlite3.connect("sentimentscope.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            text TEXT,
            sentiment TEXT,
            subreddit TEXT,
            score INTEGER,
            date DATETIME,
            link TEXT
        )
    """)
    conn.commit()
    conn.close()

# Salva un post nel database
def save_post(title, text, sentiment, subreddit, score, date, link):
    try:
        conn = sqlite3.connect("sentimentscope.db")
        cursor = conn.cursor()
        cursor.execute(
            """INSERT INTO Posts (title, text, sentiment, subreddit, score, date, link)
            VALUES (?, ?, ?, ?, ?, ?, ?)""",
            (title, text, sentiment, subreddit, score, date, link)
        )
        conn.commit()
        conn.close()
        print("Post salvato nel database SQLite.")
    except Exception as e:
        print(f"Errore nel salvataggio del post: {e}")

# Recupera tutti i post dal database
def get_all_posts():
    conn = sqlite3.connect("sentimentscope.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Posts")
    posts = cursor.fetchall()
    conn.close()
    return posts

# Inizializza il database
init_db()
