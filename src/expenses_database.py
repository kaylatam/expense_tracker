import sqlite3

# Establishing a connection - name of database: expense
connection = sqlite3.connect("expense.db")

# Helps execute SQLite Statements
cursor = connection.cursor()

# Creating the table
cursor.execute(
    """CREATE TABLE expense
(ID INTEGER PRIMARY KEY, Date DATE,
Description TEXT,
Category TEXT,
Price REAL,
MethodOfPayment TEXT)"""
)

# Actually creating the database
connection.commit()
connection.close()
