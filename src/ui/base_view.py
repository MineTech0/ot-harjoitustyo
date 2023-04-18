from tkinter import messagebox, ttk, constants


class BaseView():
    def __init__(self, root, navigate):
        self.navigate = navigate
        self._frame = ttk.Frame(master=root)

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        pass

    def show_error(self, message: str):
        messagebox.showerror("Error", message)

    def show_info(self, message: str):
        messagebox.showinfo("Info", message)
