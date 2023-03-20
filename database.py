import mysql.connector
from tkinter import *
import tkinter.messagebox as messagebox

SQL_HOST = "sql7.freesqldatabase.com"
DATABASE_USER = "sql7606287"
DATABASE_PASSWORD = "kGMMHFUyl6"
DATABASE_NAME = "sql7606287"
TABLE_NAME = 'game'

mail_user = ''

# font
FONT = ("Ariel", 18)


class Login(Tk):
    """Class Login Page"""

    def __init__(self):
        super(Login, self).__init__()

        # set up window
        self.title("Login Page")
        self.geometry("600x300")
        self.resizable(False, False)

        # Create labels and text input boxes for username and password
        self.username_label_email = Label(text="Email:", font=FONT)
        self.username_entry_email = Entry()

        self.username_label = Label(text="Username:", font=FONT)
        self.username_label.pack()
        self.username_entry = Entry()
        self.username_entry.pack()

        self.password_label = Label(text="Password:", font=FONT)
        self.password_label.pack()
        self.password_entry = Entry(show="*")
        self.password_entry.pack()

        self.login_button = Button(text="Login", command=self.login_push, font=FONT, width=3)
        self.login_button.pack()
        self.sign_button = Button(text="Sign", font=FONT, width=3, command=self.sign_push)
        self.sign_button.pack()
        self.reg_button = Button(text="Registrate", font=FONT, width=7, command=self.reg_push)

        self.mainloop()

    def login_push(self):

        # Retrieve username and password from text input boxes
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Query MySQL database to check if entered credentials are valid
        try:
            with mysql.connector.connect(host=SQL_HOST,
                                         user=DATABASE_USER,
                                         password=DATABASE_PASSWORD,
                                             database=DATABASE_NAME
                                         ) as con:
                # cursor object
                cursor = con.cursor()
                # execute query
                cursor.execute("SELECT password_hash FROM users WHERE username = %s", (username,))
                result = cursor.fetchone()
        except EXCEPTION as err:
            messagebox.showerror("Error", f"Error: {err}")
        else:
            # Check if password matches password hash from database
            if result and password == result[0]:
                # Allow user to log in
                messagebox.showinfo("Login Successful", "You have successfully logged in!")
            else:
                # Display error message if password is incorrect
                messagebox.showerror("Login Error", "Invalid username or password.")


    def sign_push(self):
        """sign push button"""
        self.username_label_email.pack(before=self.username_label)
        self.username_entry_email.pack(before=self.username_label)
        self.sign_button.config(state="disabled")
        self.reg_button.pack(after=self.sign_button)

    def reg_push(self):

        username = self.username_entry.get()
        password = self.password_entry.get()
        email_user = self.username_entry_email.get()
        if username != "" or password != "":

            try:
                with mysql.connector.connect(host=SQL_HOST,
                                             user=DATABASE_USER,
                                             password=DATABASE_PASSWORD,
                                             database=DATABASE_NAME
                                             ) as con:
                    # cursor object
                    cursor = con.cursor()
                    # execute query
                    cursor.execute(
                    "INSERT INTO `game`(`id_user`, `email`, `name`, `password`, `score`)VALUES(NULL, %s, %s, %s, %s), (NULL, 'ghffhh', 'tytnn','emnbbail@user', 0);")

            except EXCEPTION as err:
                messagebox.showerror("Login Error", f"Invalid username or password{err}")
            else:
                messagebox.showinfo("Regi Successful", "You have successfully logged in!")


login = Login()
