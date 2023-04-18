from tkinter import ttk
from services.user_service import UserService

from ui.base_view import BaseView


class LoginView(BaseView):

    def _initialize(self):
        username_label = ttk.Label(
            master=self._frame, text="Syötä käyttäjänimi:")
        password_label = ttk.Label(master=self._frame, text="Syötä salasana:")

        self._username_input = ttk.Entry(master=self._frame)
        self._password_input = ttk.Entry(master=self._frame, show="*")

        login_button = ttk.Button(
            master=self._frame,
            text="Kirjaudu",
            command=self._handle_login
        )

        register_button = ttk.Button(
            master=self._frame,
            text="Rekisteröidy",
            command=lambda: self.navigate('register')
        )

        username_label.grid(row=0, column=0)
        password_label.grid(row=1, column=0)
        self._username_input.grid(row=0, column=1)
        self._password_input.grid(row=1, column=1)
        login_button.grid(row=2, column=0)
        register_button.grid(row=2, column=1)

    def _handle_login(self):
        user_name = self._username_input.get()
        password = self._password_input.get()

        user_service = UserService()

        if user_service.login_user(user_name, password):
            self.navigate('main')
        else:
            self.show_error("Väärä käyttäjänimi tai salasana")
