from tkinter import ttk
from ui.base_view import BaseView


class MainView(BaseView):
    def _initialize(self):
        label = ttk.Label(master=self._frame, text="Tervetuloa!")
        label.grid(row=0, column=0)
