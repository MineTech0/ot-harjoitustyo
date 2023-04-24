class User():
    def __init__(self, row):
        self.user_name = row["name"]
        self.password = row["password"]

    @staticmethod
    def create_table():
        return "CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT, password TEXT)"
