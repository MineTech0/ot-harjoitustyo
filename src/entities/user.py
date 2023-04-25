class User():
    def __init__(self, row):
        self.user_name = row["name"]
        self.password = row["password"]
