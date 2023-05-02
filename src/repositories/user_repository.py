from db import get_connection
from entities.user import User


class UserRepository():

    def __init__(self):
        self._connection = get_connection()

    def get_user_by_name(self, user_name: str) -> User | None:
        """
        Returns a user entity with the given name.

        Args:
            user_name (str): name of the user

        Returns:
            User: user entity with the given name or None if no user with the given name exists
        """

        user = self._connection.execute(
            "SELECT * FROM users WHERE name = ?", (user_name,)).fetchone()

        if user:
            return User(user)
        return None

    def create_user(self, user_name: str, password: str):
        """
        Inserts a new user into the database.

        Args:
            user_name (str): name of the user
            password (str): password of the user
        """
        self._connection.execute(
            "INSERT INTO users (name, password) VALUES (?, ?)", (user_name, password))
        self._connection.commit()


user_repository = UserRepository()
