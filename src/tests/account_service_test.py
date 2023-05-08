import unittest
from init_db import init_database

from services.account_service import AccountNameTakenException, account_service
from services.user_service import user_service


class TestAccountService(unittest.TestCase):
    def setUp(self):
        init_database()
        self._account_service = account_service
        # login user
        user_service.create_user("test", "test")
        user_service.login_user("test", "test")

    def test_get_all_account_names(self):
        names = self._account_service.get_all_account_names()
        self.assertEqual(len(names), 0)

        self._account_service.add_account("test", "test", "test")
        names = self._account_service.get_all_account_names()
        self.assertEqual(len(names), 1)
        self.assertEqual(names[0], "test")

    def test_add_account(self):
        self._account_service.add_account("test", "test", "test")
        account = self._account_service.get_account("test")
        self.assertEqual(account.name, "test")
        self.assertEqual(account.user_name, "test")
        self.assertEqual(account.password, "test")

    def test_delete_account(self):
        self._account_service.add_account("test", "test", "test")
        self._account_service.delete_account("test")
        names = self._account_service.get_all_account_names()
        self.assertEqual(len(names), 0)

        self.assertEqual(len(names), 0)

    def test_no_same_name_account(self):
        self._account_service.add_account("test", "test", "test")
        self.assertRaises(
            AccountNameTakenException, self._account_service.add_account, "test", "test", "test")
