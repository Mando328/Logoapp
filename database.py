import sqlite3
import os

DB_PATH = 'diagnostyka.db'

def connect_to_db():
    """Connect to SQLite database"""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row  # Return results as dictionaries
    return conn

def init_db():
    """Initialize the database and create tables"""
    conn = connect_to_db()
    cursor = conn.cursor()
    
    # Create users table (example)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    conn.commit()
    conn.close()
    print("Database initialized successfully!")

if __name__ == "__main__":
    init_db()
