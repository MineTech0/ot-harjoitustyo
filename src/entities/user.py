from entities.base_entity import BaseEntity


class User(BaseEntity):
    def __init__(self, row):
        self.user_name = row["name"]
        self.password = row["password"]

    @staticmethod
    def create_table():
        return "CREATE TABLE users (name TEXT, password TEXT)"
