from tkinter import ttk
from services.user_service import UserNameTakenException, user_service

from ui.base_view import BaseView


class RegisterView(BaseView):

    def _initialize(self):
        username_label = ttk.Label(
            master=self._frame,
            text="Syötä käyttäjänimi:"
        )
        password_label = ttk.Label(
            master=self._frame,
            text="Syötä salasana:"
        )

        self._username_input = ttk.Entry(master=self._frame)
        self._password_input = ttk.Entry(master=self._frame, show="*")

        button = ttk.Button(
            master=self._frame,
            text="Rekisteröidy",
            command=self._handle_register
        )

        # Add padding and spacing between the elements
        username_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        password_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self._username_input.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        self._password_input.grid(row=1, column=1, padx=5, pady=5, sticky="ew")
        button.grid(row=2, column=1, padx=5, pady=5, sticky="e")

        # Bind the "Enter" key to the input fields to submit the form
        self._password_input.bind("<Return>", self._handle_register)

        # Focus the username input field
        self._username_input.focus_set()

    def _handle_register(self, event=None):
        """
        Handle the register button click event. If the inputs are valid, Navigates to login view

        Args:
            event (_type_, optional): Click event. Defaults to None.
        """
        if not self.validate_inputs():
            return

        user_name = self._username_input.get()
        password = self._password_input.get()

        try:
            user_service.create_user(user_name, password)
        except UserNameTakenException:
            self.show_error("Käyttäjänimi on jo käytössä")
            return

        self.show_info("Rekisteröityminen onnistui")

        self.navigate('login')

    def validate_inputs(self):
        """
        Validates the inputs. Shows an error message if the inputs are invalid.

        Returns:
            bool: True if the inputs are valid, False otherwise
        """
        if len(self._username_input.get()) < 3:
            self.show_error(
                "Käyttäjänimen tulee olla vähintään 3 merkkiä pitkä")
            return False
        if len(self._password_input.get()) < 5:
            self.show_error("Salasanan tulee olla vähintään 5 merkkiä pitkä")
            return False
        return True
