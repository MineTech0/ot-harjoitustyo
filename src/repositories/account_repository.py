from db import get_connection
from entities.account import Account


class AccountRepository:
    def __init__(self):
        self._connection = get_connection()

    def get_all_account_names(self, user_id: int):
        """
        Returns a list of all account names in the database.

        Args:
            user_id (int): id of the current user

        Returns:
            list: list of all account names in the database
        """
        result = self._connection.execute(
            """
            SELECT name FROM accounts WHERE user_id = ?
            """, (str(user_id))).fetchall()
        return [row[0] for row in result]

    def add_account(self, account: str, username: str, password: str, user_id: int):
        """
        Inserts a new account into the database.

        Args:
            account (str): name of the account
            username (str): username of the account
            password (str): password of the account
            user_id (int): id of the current user
        """

        self._connection.execute(
            """INSERT INTO accounts (name, user_name, password, user_id) 
            VALUES (?, ?, ?, ?)""", (account, username, password, str(user_id)))
        self._connection.commit()
        print("Account added")

    def get_account(self, account: str, user_id: int) -> Account:
        """
        Returns an account entity with the given name.

        Args:
            account (str): name of the account
            user_id (int): id of the current user

        Returns:
            _type_: _description_
        """
        result = self._connection.execute(
            "SELECT name, user_name, password FROM accounts WHERE name = ? AND user_id = ?", (account, str(user_id))).fetchone()
        return Account(result)

    def delete_account(self, account_name, user_id: int):
        """
        Deletes an account from the database.

        Args:
            account_name (str): name of the account to be deleted
            user_id (int): id of the current user
        """
        self._connection.execute(
            "DELETE FROM accounts WHERE name = ? AND user_id = ?", (account_name, str(user_id)))
        self._connection.commit()
        print("Account deleted")


account_repository = AccountRepository()
