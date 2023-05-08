from sqlite3 import Connection
import db


def create_tables(connection: Connection):
    """
    Create all tables in the database.

    Args:
        connection (Connection): connection to the database
    """

    connection.execute(
        "CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT, password TEXT)")
    connection.commit()
    print("Created users table.")

    connection.execute(
        """CREATE TABLE accounts 
        (id INTEGER PRIMARY KEY, name TEXT UNIQUE,
        user_name TEXT, password TEXT,
        user_id INTEGER,
        FOREIGN KEY(user_id) REFERENCES users(id))""")
    connection.commit()
    print("Created accounts table.")


def drop_tables(connection):
    """
    Drop all tables from the database.

    """
    connection.execute("DROP TABLE IF EXISTS accounts")
    connection.commit()
    connection.execute("DROP TABLE IF EXISTS users")
    connection.commit()
    print("Dropped all tables.")


def init_database():
    connection = db.get_connection()

    drop_tables(connection)

    create_tables(connection)

    print("Database initialized successfully.")


if __name__ == "__main__":
    init_database()
