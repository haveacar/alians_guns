import mysql.connector
from tkinter import *
import tkinter.messagebox as messagebox

SQL_HOST = "sql7.freesqldatabase.com"
DATABASE_USER = "sql7606287"
DATABASE_PASSWORD = "kGMMHFUyl6"
DATABASE_NAME = "sql7606287"
TABLE_NAME = 'game'

mail_user = ''

# constants
FONT = ("Courier", 18)
YELLOW = "#f7f5dd"



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
        self.flag_game= FALSE
        self.max_score = 0


        self.mainloop()


    def login_push(self):

        # Retrieve username and password from text input boxes
        user_email = self.username_entry_email.get()
        # check case empty input
        if len(user_email)==0:
            messagebox.showerror("Error", "You need something to write")

        else:
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
                    cursor.execute("SELECT * FROM game WHERE email=%s ", (user_email,))
                    result = cursor.fetchone()
                    print(result)
            except EXCEPTION as err:
                messagebox.showerror("Error", f"Error: {err}")
            else:
                # Check if password matches password hash from database
                if result:
                    # Allow user to log in
                    messagebox.showinfo("Login Successful", f"You have successfully logged in!\n{result[1]}\nYour MAX score: {result[2]}")
                    self.flag_game = True
                    self.max_score =int(result[2])
                    print(self.max_score)
                else:
                    # Display error message if password is incorrect
                    messagebox.showerror("Login Error", "Invalid username or password.")


    def sign_push(self):
        # widgets
        self.sign_button.config(state="disabled")
        self.username_label.pack(before=self.username_label_email)
        self.username_entry.pack(before=self.username_label_email)
        self.reg_button.pack()

    def registration(self):
        # get from entry
        user_email = self.username_entry_email.get()
        user_name=self.username_entry.get()
        user_score =0

        # check case empty input
        if len(user_email)==0 or len(user_name) == 0:
            messagebox.showerror("Error", "You need something to write")

        else:
                with mysql.connector.connect(host=SQL_HOST,
                                             user=DATABASE_USER,
                                             password=DATABASE_PASSWORD,
                                             database=DATABASE_NAME
                                             ) as con:
                    # cursor object
                    cursor = con.cursor()
                    # execute query
                    cursor.execute("INSERT INTO game (email, name, score) VALUES (%s, %s, %s)", (user_email, user_name, user_score))

                messagebox.showinfo("Registration Successful",
                                    f"You have successfully registered\n{user_name}\nStart Play")

    def high_score(self):
        return self.max_score