from repositories.account_repository import account_repository
from services.user_service import user_service
import utils


class AccountNameTakenException(Exception):
    pass


class AccountService():

    def get_all_account_names(self):
        """
        Returns a list of all account names in the database.

        Returns:
            list: list of all account names in the database

        """
        user_id = user_service.get_current_user().id
        return account_repository.get_all_account_names(user_id)

    def add_account(self, account: str, username: str, password: str):
        """
        Persists a new account to the database. Encrypts the password before storing it.
        Raises an AccountNameTakenException if the account name is already taken.

        Args:
            account (str): account name
            username (str): username
            password (str): password

        Raises:
            AccountNameTakenException: if the account name is already taken
        """
        # check if account name is taken
        if account in self.get_all_account_names():
            raise AccountNameTakenException
        else:
            password = utils.encrypt(
                password, user_service.get_encryption_password())
            user_id = user_service.get_current_user().id
            account_repository.add_account(
                account, username, password, user_id)

    def get_account(self, account_name: str):
        """
        Returns an account entity with the given name. Decrypts the password before returning it.

        Args:
            account (str): name of the account

        Returns:
            Account: account entity with the given name
        """
        user_id = user_service.get_current_user().id
        account = account_repository.get_account(account_name, user_id)
        account.password = utils.decrypt(
            account.password, user_service.get_encryption_password())
        return account

    def delete_account(self, account_name: str):
        """
        Deletes an account from the database.

        Args:
            account_name (str): name of the account to be deleted
        """
        user_id = user_service.get_current_user().id
        account_repository.delete_account(account_name, user_id)


account_service = AccountService()
