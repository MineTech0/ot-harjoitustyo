from repositories.account_repository import account_repository
from services.user_service import user_service
import utils

class AccountNameTakenException(Exception):
    pass

class AccountService():

    def get_all_account_names(self):
        return account_repository.get_all_account_names()

    def add_account(self, account, username, password):
        #check if account name is taken
        if account in self.get_all_account_names():
            raise AccountNameTakenException
        else:
            password = utils.encrypt(
                password, user_service.get_encryption_password())
            account_repository.add_account(account, username, password)

    def get_account(self, account):
        account = account_repository.get_account(account)
        account.password = utils.decrypt(
            account.password, user_service.get_encryption_password())
        return account
    
    def delete_account(self, account_name):
        account_repository.delete_account(account_name)


account_service = AccountService()
