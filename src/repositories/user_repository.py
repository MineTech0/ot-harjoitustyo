from db import get_connection
from entities.user import User


class UserRepository():

    def __init__(self):
        self._connection = get_connection()

    def get_user_by_name(self, user_name):
        # Get user from database
        user = self._connection.execute(
            "SELECT * FROM users WHERE name = ?", (user_name,)).fetchone()
        # Return user
        if user:
            return User(user)
        return None

    def create_user(self, user_name, password):
        # Create user
        self._connection.execute(
            "INSERT INTO users (name, password) VALUES (?, ?)", (user_name, password))
        # Commit changes
        self._connection.commit()


user_repository = UserRepository()
