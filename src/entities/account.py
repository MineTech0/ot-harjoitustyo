class Account():
    def __init__(self, row):
        self.name = row["name"]
        self.user_name = row["user_name"]
        self.password = row["password"]
