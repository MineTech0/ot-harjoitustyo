from repositories.account_repository import account_repository
from services.user_service import user_service
import utils


class AccountService():

    def get_all_account_names(self):
        return account_repository.get_all_account_names()

    def add_account(self, account, username, password):
        password = utils.encrypt(password, user_service.encryption_password)
        account_repository.add_account(account, username, password)

    def get_account(self, account):
        account = account_repository.get_account(account)
        account.password = utils.decrypt(
                account.password, user_service.encryption_password)
        return account

account_service = AccountService()
