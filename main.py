from database import connect_to_db, init_db

# Initialize database on first run
init_db()

# Test connection
conn = connect_to_db()
cursor = conn.cursor()

# Example: Get all tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print("Tables in database:", tables)

conn.close()
