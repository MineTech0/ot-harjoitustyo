from ui.base_view import BaseView
from ui.login_view import LoginView
from ui.main_view import MainView
from ui.register_view import RegisterView


class UI:
    def __init__(self, root):
        self._root = root
        self._current_view = BaseView(root, self.navigate)

    def start(self):
        self._show_login_view()

    def navigate(self, view):
        self._current_view.destroy()
        if view == "login":
            self._show_login_view()
        elif view == "register":
            self._show_register_view()
        elif view == "main":
            self._show_main_view()

    def _show_login_view(self):
        self._current_view = LoginView(
            self._root,
            self.navigate
        )

        self._current_view.pack()

    def _show_register_view(self):
        self._current_view = RegisterView(
            self._root,
            self.navigate
        )

        self._current_view.pack()

    def _show_main_view(self):
        self._root.geometry("800x500")
        self._current_view = MainView(
            self._root,
            self.navigate
        )

        self._current_view.pack()
