class User():
    def __init__(self, row):
        self.id = row["id"]
        self.user_name = row["name"]
        self.password = row["password"]
