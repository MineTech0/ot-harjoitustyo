from tkinter import ttk
from services.user_service import UserService

from ui.base_view import BaseView


class RegisterView(BaseView):

    def _initialize(self):
        username_label = ttk.Label(
            master=self._frame, text="Syötä käyttäjänimi:")
        password_label = ttk.Label(master=self._frame, text="Syötä salasana:")

        self._username_input = ttk.Entry(master=self._frame)
        self._password_input = ttk.Entry(master=self._frame, show="*")

        button = ttk.Button(
            master=self._frame,
            text="Rekisteröidy",
            command=self._handle_register
        )

        username_label.grid(row=0, column=0)
        password_label.grid(row=1, column=0)
        self._username_input.grid(row=0, column=1)
        self._password_input.grid(row=1, column=1)
        button.grid(row=2, column=1)

    def _handle_register(self):
        user_service = UserService()

        user_name = self._username_input.get()
        password = self._password_input.get()

        user_service.create_user(user_name, password)

        self.show_info("Rekisteröityminen onnistui")

        self.navigate('login')
