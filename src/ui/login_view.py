from tkinter import ttk
from services.user_service import user_service

from ui.base_view import BaseView


class LoginView(BaseView):

    def _initialize(self):
        username_label = ttk.Label(
            master=self._frame, text="Syötä käyttäjänimi:")
        password_label = ttk.Label(master=self._frame, text="Syötä salasana:")
        self._username_input = ttk.Entry(master=self._frame)
        self._password_input = ttk.Entry(master=self._frame, show="*")
        login_button = ttk.Button(
            master=self._frame, text="Kirjaudu", command=self._handle_login)
        register_button = ttk.Button(
            master=self._frame, text="Rekisteröidy", command=lambda: self.navigate('register'))

        username_label.grid(row=0, column=0, padx=5, pady=5)
        self._username_input.grid(row=0, column=1, padx=5, pady=5)
        password_label.grid(row=1, column=0, padx=5, pady=5)
        self._password_input.grid(row=1, column=1, padx=5, pady=5)
        login_button.grid(row=2, column=0, columnspan=2,
                          padx=5, pady=5, sticky="we")
        register_button.grid(row=3, column=0, columnspan=2,
                             padx=5, pady=5, sticky="we")

        # Focus the username input field
        self._username_input.focus_set()

        # Bind the "Enter" key to the input fields to submit the form
        self._password_input.bind("<Return>", self._handle_login)

    def _handle_login(self, event=None):
        """
        Handle the login button click event. If the inputs are valid, Navigates to main view

        Args:
            event (_type_, optional): Click event. Defaults to None.
        """
        user_name = self._username_input.get()
        password = self._password_input.get()

        if user_service.login_user(user_name, password):
            self.navigate('main')
        else:
            self.show_error("Väärä käyttäjänimi tai salasana")
