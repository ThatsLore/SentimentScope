import sqlite3

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
            link TEXT,
            keyword TEXT
        )
    """)
    conn.commit()
    conn.close()

def save_post(title, text, sentiment, subreddit, score, date, link, keyword):
    try:
        conn = sqlite3.connect("sentimentscope.db")
        cursor = conn.cursor()
        # evita duplicati controllando il link
        cursor.execute("SELECT id FROM Posts WHERE link = ?", (link,))
        if cursor.fetchone():
            print("Post già presente, skip.")
            conn.close()
            return
        cursor.execute(
            """INSERT INTO Posts (title, text, sentiment, subreddit, score, date, link, keyword)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
            (title, text, sentiment, subreddit, score, date, link, keyword)
        )
        conn.commit()
        conn.close()
        print("Post salvato.")
    except Exception as e:
        print(f"Errore nel salvataggio: {e}")

def get_posts_by_keyword(keyword):
    conn = sqlite3.connect("sentimentscope.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Posts WHERE keyword = ?", (keyword,))
    posts = cursor.fetchall()
    conn.close()
    return posts

def get_all_posts():
    conn = sqlite3.connect("sentimentscope.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Posts")
    posts = cursor.fetchall()
    conn.close()
    return posts

init_db()