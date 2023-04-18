import importlib
import inspect
import os
from sqlite3 import Connection
import db
from entities.base_entity import BaseEntity
from config import DATABASE_FILE_PATH


def create_tables(connection: Connection):
    """
    Creates alla tables from the entities folder.
    
    *generated with ChatGPT*

    Args:
        connection (Connection): db connection
    """
    print("Creating tables...")
    # Get a list of all .py files in the entities folder
    entity_files = [f for f in os.listdir("src/entities") if f.endswith(".py")]

    # Loop through the files and import the modules dynamically
    for file in entity_files:
        module_name = file[:-3]  # Remove the .py extension
        module = importlib.import_module(f"entities.{module_name}")

        # Loop through the classes in the module and create the tables
        for _, obj in inspect.getmembers(module, inspect.isclass):
            if issubclass(obj, BaseEntity):
                sql_statement = obj.create_table()
                if sql_statement:
                    print(f"Executing: {sql_statement}")
                    connection.execute(sql_statement)
                    connection.commit()


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
