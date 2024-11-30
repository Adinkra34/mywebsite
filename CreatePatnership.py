import sqlite3

# Connect to the SQLite database (it will create the file if it doesn't exist)
conn = sqlite3.connect('partnerships.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create the partnerships table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS partnerships (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL,
        organization TEXT,
        message TEXT NOT NULL
    )
''')

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Database and table created successfully.")
