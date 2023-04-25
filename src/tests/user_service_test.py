import unittest
from init_db import init_database

from services.user_service import user_service


class TestUserService(unittest.TestCase):
    def setUp(self):
        init_database()
        self._user_service = user_service

    def test_create_user(self):
        self._user_service.create_user("test", "test")
        user = self._user_service.get_user_by_name("test")
        self.assertNotEqual(user, None)
        if user:
            self.assertEqual(user.user_name, "test")

    def test_login_user(self):
        self._user_service.create_user("test", "test")
        self.assertTrue(self._user_service.login_user("test", "test"))
        self.assertFalse(self._user_service.login_user("test", "wrong"))
        self.assertFalse(self._user_service.login_user("wrong", "test"))
