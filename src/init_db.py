import db
from sqlite3 import Connection

def create_tables(connection: Connection):
    print("Creating tables...")
    pass

def drop_tables(connection: Connection):
    print("Dropping tables...")
    pass
    
def init_database():

    connection = db.get_connection()

    drop_tables(connection)
    create_tables(connection)
    
    print("Database initialized successfully.")


if __name__ == "__main__":
    init_database()