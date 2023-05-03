import sqlite3

con = sqlite3.connect("bb9f9d7b", check_same_thread=False)


def create_tables():
    cur = con.cursor()
    cur.execute("""CREATE TABLE short_link(short_url TEXT NOT NULL unique, original_url TEXT NOT NULL)""")
    cur.close()
    con.commit()


class Database:
    def __init__(self):
        pass


def insert(url, short_url):
    try:
        con.execute("INSERT INTO short_link (short_url, original_url) \
              VALUES (?, ?)", (short_url, url))
        con.commit()
    except Exception as e:
        print(e)


def get_url(short_url):
    try:
        cur = con.cursor()
        cur.execute("SELECT original_url FROM short_link where short_url = ?", (short_url, ))
        original_url = cur.fetchone()
        return original_url[0] if original_url else None
    except Exception as e:
        print(e)

    return None
