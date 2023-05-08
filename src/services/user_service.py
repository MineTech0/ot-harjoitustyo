from entities.user import User
from repositories.user_repository import user_repository
import utils


class UserNameTakenException(Exception):
    pass


class UserService():

    def __init__(self) -> None:
        """
        Initializes the UserService with no user logged in.
        """
        self.encryption_password = None
        self.current_user = None

    def get_encryption_password(self):
        """
        Returns the encryption password of the currently logged in user.

        Raises:
            ValueError: if no user is logged in

        Returns:
            str: encryption password of the currently logged in user
        """
        if self.encryption_password is None:
            raise ValueError("No user logged in")
        return self.encryption_password

    def get_current_user(self) -> User:
        """
        Returns the currently logged in user.

        Raises:
            ValueError: if no user is logged in

        Returns:
            User: currently logged in user
        """
        if self.current_user is None:
            raise ValueError("No user logged in")
        return self.current_user

    def get_user_by_name(self, user_name: str) -> User | None:
        """
        Gets the user by name.

        Args:
            user_name (str): name of the user

        Returns:
            User | None: user with the given name or None if no user with the given name exists
        """
        return user_repository.get_user_by_name(user_name)

    def create_user(self, user_name: str, password: str):
        """
        Creates a new user with the given name and password. Hashes the password before storing it.

        Args:
            user_name (str): name of the user
            password (str): password of the user

        Raises:
            UserNameTakenException: _description_
        """
        # check if username is taken
        if user_repository.get_user_by_name(user_name) is not None:
            raise UserNameTakenException

        hashed_password = utils.hash_password(password)
        user_repository.create_user(user_name, hashed_password)

    def login_user(self, user_name: str, password: str) -> bool:
        """
        Logs in the user with the given name and password. 
        Sets the encryption password to the given password.

        Args:
            user_name (str): name of the user
            password (str): given password

        Returns:
            bool: True if the user was logged in successfully, False otherwise
        """
        user = user_repository.get_user_by_name(user_name)
        if user is None:
            return False
        logged_in = utils.check_password(password, user.password)
        if logged_in:
            self.encryption_password = password
            self.current_user = user
        return logged_in

    def logout_user(self):
        """
        Logs out the currently logged in user.
        """
        self.encryption_password = None
        self.current_user = None


user_service = UserService()
