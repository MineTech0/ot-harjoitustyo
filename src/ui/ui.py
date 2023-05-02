from ui.base_view import BaseView
from ui.login_view import LoginView
from ui.main_view import MainView
from ui.register_view import RegisterView


class UI:
    def __init__(self, root):
        self._root = root
        self._current_view = BaseView(root, self.navigate)

    def start(self):
        """
        Starts the UI by showing the login view
        """
        self._show_login_view()

    def navigate(self, view: str):
        """
        This function is used to navigate between views. It is passed to the views as a parameter.

        Args:
            view (str): name of the view to navigate to
        """
        self._current_view.destroy()
        if view == "login":
            self._show_login_view()
        elif view == "register":
            self._show_register_view()
        elif view == "main":
            self._show_main_view()

    def _show_login_view(self):
        """
        Renders the login view.
        """
        self._root.geometry("400x200")
        self._current_view = LoginView(
            self._root,
            self.navigate
        )

        self._current_view.pack()

    def _show_register_view(self):
        """
        Renders the register view.
        """
        self._root.geometry("400x200")
        self._current_view = RegisterView(
            self._root,
            self.navigate
        )

        self._current_view.pack()

    def _show_main_view(self):
        """
        Renders the main view.
        """
        self._root.geometry("700x300")
        self._current_view = MainView(
            self._root,
            self.navigate
        )

        self._current_view.pack()
