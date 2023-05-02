from tkinter import messagebox, ttk, constants


class BaseView():
    def __init__(self, root, navigate):
        """
        Constructor for BaseView
        creates a frame and sets up the base view for all views

        Args:
            root: tk root
            navigate: function that takes a view name as a parameter and navigates to that view
        """
        self.navigate = navigate
        self.root = root
        self._frame = ttk.Frame(master=root)

        # add padding to the frame
        self._frame['padding'] = (20, 10)

        # initialize the view
        self._initialize()

    def pack(self):
        """
        Is called from ui when the view should be shown
        """
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """
        Is called from ui when the view should be destroyed
        """
        self._frame.destroy()

    def _initialize(self):
        """
        This function is called in the constructor and should be overridden in the child classes
        Use this function to initialize the view and add elements to the frame
        """
        pass

    def show_error(self, message: str):
        """
        Shows an error message popup

        Args:
            message (str): error message
        """
        messagebox.showerror("Error", message)

    def show_info(self, message: str):
        """
        Shows an info message popup

        Args:
            message (str): info message
        """
        messagebox.showinfo("Info", message)
