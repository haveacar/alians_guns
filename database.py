import pathlib
import sqlite3
from tkinter import *
import tkinter.messagebox as messagebox

mail_user = ''

# constants
FONT = ("Courier", 18)
YELLOW = "#f7f5dd"

# database patch
DB_URL = pathlib.Path(__file__).parent.joinpath("data.db")


class Login(Tk):
    """Class Login Page"""

    def __init__(self):
        super(Login, self).__init__()

        # set up window
        self.title("Login Page")
        self.config(bg=YELLOW)
        self.geometry("600x300")
        self.resizable(False, False)

        # Create labels and text input boxes for username and password
        self.username_label_email = Label(text="Email:", font=FONT, background=YELLOW, foreground='red')
        self.username_label_email.pack()

        self.username_entry_email = Entry()
        self.username_entry_email.pack()

        self.username_label = Label(text="Name:", font=FONT, background=YELLOW, foreground='red')
        self.username_entry = Entry()

        self.login_button = Button(text="Login", command=self.login_push, font=FONT, width=3)
        self.login_button.pack()
        self.sign_button = Button(text="New Game", font=FONT, width=7, command=self.sign_push)
        self.sign_button.pack()
        self.reg_button = Button(text="Registration", font=FONT, width=9, command=self.registration)

        # start game flag
        self.flag_game = FALSE
        self.max_score = 0
        self.mail = ""

        self.mainloop()

    def sql_request(self, n_cursor, query_result=False):
        """
        sql request func
        :param n_cursor: string sql request
        """

        try:
            with sqlite3.connect(DB_URL) as sqlite_connection:  # Connect to database
                # Create cursor object
                cursor = sqlite_connection.cursor()
                # Execute SQL query
                cursor.execute(n_cursor)
                # Fetch result
                if query_result:
                    res = cursor.fetchall()
                else:
                    res = None
                pass
                return res
        except sqlite3.Error as err:
            print("******", err)
            messagebox.showerror("Error", f"Error: {err}")
        else:
            print("***Complete***")

    def login_push(self):
        """Func Login, get entry and Mysql request"""

        # Retrieve username and password from text input boxes
        user_email = self.username_entry_email.get()
        # check case empty input
        if len(user_email) == 0:
            messagebox.showerror("Error", "You need something to write")

        else:
            # select sql request
            request = f'''SELECT * from "game"
                                where email  = '$mail$';'''
            request = request.replace('$mail$', user_email)

            result = self.sql_request(request, query_result=True)

            # Check if password matches password hash from database
            if result:
                # Allow user to log in
                messagebox.showinfo("Login Successful",
                                    f"You have successfully logged in!\n{result[1]}\nYour MAX score: {result[2]}")
                self.flag_game = True
                self.max_score = int(result[2])
                self.mail = result[0]
            else:
                # Display error message if password is incorrect
                messagebox.showerror("Login Error", "Invalid username or password.")

    def sign_push(self):
        """Func disable widgets and display widgets"""
        # widgets
        self.sign_button.config(state="disabled")
        self.username_label.pack(before=self.username_label_email)
        self.username_entry.pack(before=self.username_label_email)
        self.reg_button.pack()

    def registration(self):
        """Func Reg, get entry and Mysql request, Insert to database"""
        # get from entry
        user_email = self.username_entry_email.get()
        user_name = self.username_entry.get()
        user_score = 0

        # check case empty input
        if len(user_email) == 0 or len(user_name) == 0:
            messagebox.showerror("Error", "You need something to write")

        else:

            request = f"""INSERT OR REPLACE INTO "game" ("email","name","score") VALUES ("$mail$","$name$", {user_score});"""
            request = request.replace('$mail$', user_email)
            request = request.replace('$name$', user_name)

            self.sql_request(request, query_result=False)
            messagebox.showinfo("Registration Successful",
                                f"You have successfully registered\n{user_name.upper()}\nStart Play")
            self.flag_game = True
            self.mail = user_email

    def high_score(self):
        """
        func return high score
        :return: int(max score)
        """

        return self.max_score, self.mail
