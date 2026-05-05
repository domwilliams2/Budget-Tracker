import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent / "budget.db"

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn

#create tables
def init_db():
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    with get_connection() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS account (
                account_id TEXT PRIMARY KEY NOT NULL,
                name TEXT NOT NULL,
                balance INTEGER NOT NULL,
                account_type TEXT NOT NULL
            )
        """)
        conn.execute("""
            CREATE TABLE IF NOT EXISTS category (
                category_id TEXT PRIMARY KEY NOT NULL,
                name TEXT NOT NULL,
                color TEXT
            )
        """)
        conn.execute("""
            CREATE TABLE IF NOT EXISTS transactions (
                transaction_id TEXT PRIMARY KEY NOT NULL,
                amount INTEGER NOT NULL,
                date TEXT NOT NULL,
                description TEXT NOT NULL,
                type TEXT NOT NULL,
                account_id TEXT NOT NULL,
                category_id TEXT,
                FOREIGN KEY (account_id) REFERENCES account(account_id) ON DELETE CASCADE,
                FOREIGN KEY (category_id) REFERENCES category(category_id) ON DELETE SET NULL
            )
        """)