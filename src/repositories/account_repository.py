from db import get_connection
from entities.account import Account


class AccountRepository:
    def __init__(self):
        self._connection = get_connection()

    def get_all_account_names(self):
        """
        Returns a list of all account names in the database.

        Returns:
            list: list of all account names in the database
        """
        result = self._connection.execute(
            "SELECT name FROM accounts").fetchall()
        return [row[0] for row in result]

    def add_account(self, account: str, username: str, password: str):
        """
        Inserts a new account into the database.

        Args:
            account (str): name of the account
            username (str): username of the account
            password (str): password of the account
        """

        self._connection.execute(
            """INSERT INTO accounts (name, user_name, password) 
            VALUES (?, ?, ?)""", (account, username, password))
        self._connection.commit()
        print("Account added")

    def get_account(self, account: str) -> Account:
        """
        Returns an account entity with the given name.

        Args:
            account (str): name of the account

        Returns:
            _type_: _description_
        """
        result = self._connection.execute(
            "SELECT name, user_name, password FROM accounts WHERE name = ?", (account,)).fetchone()
        return Account(result)

    def delete_account(self, account_name):
        """
        Deletes an account from the database.

        Args:
            account_name (str): name of the account to be deleted
        """
        self._connection.execute(
            "DELETE FROM accounts WHERE name = ?", (account_name,))
        self._connection.commit()
        print("Account deleted")


account_repository = AccountRepository()
