from db import get_connection
from entities.account import Account


class AccountRepository:
    def __init__(self):
        self._connection = get_connection()

    def get_all_account_names(self):
        result = self._connection.execute(
            "SELECT name FROM accounts").fetchall()
        return [row[0] for row in result]

    def add_account(self, account, username, password):
        self._connection.execute(
            """INSERT INTO accounts (name, user_name, password) 
            VALUES (?, ?, ?)""", (account, username, password))
        self._connection.commit()
        print("Account added")

    def get_account(self, account):
        result = self._connection.execute(
            "SELECT name, user_name, password FROM accounts WHERE name = ?", (account,)).fetchone()
        return Account(result)

    def delete_account(self, account_name):
        self._connection.execute(
            "DELETE FROM accounts WHERE name = ?", (account_name,))
        self._connection.commit()
        print("Account deleted")

account_repository = AccountRepository()
