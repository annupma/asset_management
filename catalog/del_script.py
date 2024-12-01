import sqlite3

# Connect to the SQLite database
db_path = r'C:\Users\b0317568\OneDrive - Airtelworld\Project\Hardware_Assest_Management.db'  # Replace with your database path
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Fetch all table names
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

# Drop each table
for table_name in tables:
    print(f"Dropping table: {table_name[0]}")
    cursor.execute(f"DROP TABLE IF EXISTS {table_name[0]}")

# Commit changes and close connection
conn.commit()
conn.close()

print("All tables deleted.")
