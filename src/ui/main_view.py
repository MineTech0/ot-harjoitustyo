from tkinter import ttk
import tkinter as tk
from ui.base_view import BaseView
from services.account_service import account_service


class MainView(BaseView):
    def _initialize(self):
        accounts = account_service.get_all_account_names()

        # create listbox to display websites
        # create a label for the website listbox
        self.list_title = ttk.Label(
            master=self._frame, text="Tilit:")
        self.list_title.grid(
            row=0, column=0, padx=10, pady=10, sticky='w')

        # create a listbox for the website list
        self.website_listbox = tk.Listbox(master=self._frame)
        for website in accounts:
            self.website_listbox.insert(tk.END, website)
        self.website_listbox.bind('<<ListboxSelect>>', self.show_passwords)
        self.website_listbox.grid(
            row=1, column=0, rowspan=4, padx=10, pady=10, sticky='nsew')

        # create a label frame for the account details
        self.details_frame = ttk.LabelFrame(
            master=self._frame, text="Tilin tiedot:")
        self.details_frame.grid(
            row=0, column=1, rowspan=4, padx=10, pady=10, sticky='nsew')

        # create labels and text boxes to display username and password
        self.username_label = ttk.Label(
            master=self.details_frame, text="Käyttäjänimi:")
        self.username_label.grid(
            row=0, column=0, padx=10, pady=10, sticky='w')
        self.username_textbox = ttk.Entry(master=self.details_frame)
        self.username_textbox.grid(
            row=0, column=1, padx=10, pady=10, sticky='ew')
        self.password_label = ttk.Label(
            master=self.details_frame, text="Salasana:")
        self.password_label.grid(
            row=1, column=0, padx=10, pady=10, sticky='w')
        self.password_textbox = ttk.Entry(
            master=self.details_frame, show='*')
        self.password_textbox.grid(
            row=1, column=1, padx=10, pady=10, sticky='ew')
        self.password_show_button = ttk.Button(
            master=self.details_frame, text="Näytä", command=self.toggle_show)
        self.password_show_button.grid(
            row=1, column=2, padx=10, pady=10, sticky='e')
        self.account_name_label = ttk.Label(
            master=self.details_frame, text="Tilin nimi")
        self.account_name_label.grid(
            row=2, column=0, padx=10, pady=10, sticky='w')
        self.account_name_textbox = ttk.Entry(master=self.details_frame)
        self.account_name_textbox.grid(
            row=2, column=1, padx=10, pady=10, sticky='ew')

        # create button to add new account
        self.add_account_button = ttk.Button(
            master=self.details_frame, text="Lisää tili", command=self.add_account)
        self.add_account_button.grid(
            row=3, column=1, padx=10, pady=10, sticky='e')
        # create button to delete account
        self.delete_account_button = ttk.Button(
            master=self.details_frame, text="Poista tili", command=self.delete_account)
        self.delete_account_button.grid(
            row=3, column=0, padx=10, pady=10, sticky='w')
    def show_passwords(self, event):
        # get selected website
        selected_account = self.website_listbox.get(
            self.website_listbox.curselection())

        # get username and password for selected website
        account = account_service.get_account(selected_account)

        self.password_textbox.configure(show='*')
        self.password_show_button.configure(text='Näytä')

        # display username and password in text boxes
        self.username_textbox.delete(0, tk.END)
        self.username_textbox.insert(0, account.user_name)
        self.password_textbox.delete(0, tk.END)
        self.password_textbox.insert(0, account.password)
        self.account_name_textbox.delete(0, tk.END)
        self.account_name_textbox.insert(0, account.name)

    def update_account_list(self):
        # clear listbox
        self.website_listbox.delete(0, tk.END)

        # get all account names
        accounts = account_service.get_all_account_names()

        # insert account names into listbox
        for account in accounts:
            self.website_listbox.insert(tk.END, account)

    def add_account(self):
        if not self.validate_fields():
            return
        # get website, username, and password from text boxes
        account = self.account_name_textbox.get()
        username = self.username_textbox.get()
        password = self.password_textbox.get()

        # add new account to account service
        try:
            account_service.add_account(account, username, password)
        except AccountNameTakenException:
            self.show_error("Tilin nimi on jo käytössä")
            return

        # update listbox and clear text boxes
        self.update_account_list()

        self.username_textbox.delete(0, tk.END)
        self.password_textbox.delete(0, tk.END)
        self.account_name_textbox.delete(0, tk.END)
        self.username_textbox.delete(0, tk.END)
        self.password_textbox.delete(0, tk.END)
        self.account_name_textbox.delete(0, tk.END)

    def toggle_show(self):
        if self.password_textbox['show'] == '':
            self.password_textbox.configure(show='*')
            self.password_show_button.configure(text='Näytä')
        else:
            self.password_textbox.configure(show='')
            self.password_show_button.configure(text='Piilota')

    def validate_fields(self):
        if self.username_textbox.get() == '':
            self.show_error('Käyttäjänimi ei voi olla tyhjä')
            return False
        if self.password_textbox.get() == '':
            self.show_error('Salasana ei voi olla tyhjä')
            return False
        if self.account_name_textbox.get() == '':
            self.show_error('Tilin nimi ei voi olla tyhjä')
            return False
        return True
