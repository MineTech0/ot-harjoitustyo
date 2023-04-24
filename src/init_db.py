import os
from sqlite3 import Connection
import db
from config import DATABASE_FILE_PATH


def create_tables(connection: Connection):
    connection.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT, password TEXT)")
    connection.execute("CREATE TABLE accounts (id INTEGER PRIMARY KEY, name TEXT, user_name TEXT, password TEXT, user_id INTEGER, FOREIGN KEY(user_id) REFERENCES users(id))")


def drop_db():
    """
    Deletes the database
    
    """
    print("Deleting database...", DATABASE_FILE_PATH)
    path = os.path.join(DATABASE_FILE_PATH)
    if os.path.exists(path):
        os.remove(path)


def init_database():

    drop_db()
    
    connection = db.get_connection()

    create_tables(connection)

    print("Database initialized successfully.")


if __name__ == "__main__":
    init_database()
