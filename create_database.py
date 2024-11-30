import sqlite3

# Connect to the SQLite database (this will create donations.db file in your project directory)
conn = sqlite3.connect('donations.db')
cursor = conn.cursor()

# Create the donations table if it doesn’t exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS donations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name TEXT NOT NULL,
        email TEXT NOT NULL,
        phone TEXT NOT NULL
    )
''')

# Commit changes and close the connection
conn.commit()
conn.close()

print("Database and table created successfully.")
