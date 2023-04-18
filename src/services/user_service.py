from repositories.user_repository import user_repository
import utils


class UserService():

    def get_user_by_name(self, user_name):
        return user_repository.get_user_by_name(user_name)

    def create_user(self, user_name, password):
        password = utils.hash_password(password)
        user_repository.create_user(user_name, password)

    def login_user(self, user_name, password):
        user = user_repository.get_user_by_name(user_name)
        if user is None:
            return False
        return utils.check_password(password, user.password)

user_service = UserService()
