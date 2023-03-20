import mysql.connector
from tkinter import *
import tkinter.messagebox as messagebox

SQL_HOST = "sql7.freesqldatabase.com"
DATABASE_USER = "sql7606287"
DATABASE_PASSWORD = "kGMMHFUyl6"
DATABASE_NAME = "sql7606287"
TABLE_NAME = 'game'

mail_user = ''
SQL_QUERY = f'SELECT * FROM {TABLE_NAME} WHERE mail="{mail_user}";'
# font
FONT = ("Ariel", 18)


"""def request(sql_req, result = False):
    try:
        with mysql.connector.connect(host=SQL_HOST,
                                         user=DATABASE_USER,
                                         password=DATABASE_PASSWORD,
                                         database=DATABASE_NAME
                                         ) as con:
            # cursor object
            cursor = con.cursor()
            # execute query
            cursor.execute(sql_req)
            if result:
                query_result = cursor.fetchall()
                return query_result

    except Exception as err:
        print("Error: ", err)
        return False"""

class Login(Tk):
    """Class Login Page"""
    def __init__(self):
        super(Login, self).__init__()


        # set up window
        self.title("Login Page")
        self.geometry("600x300")
        self.resizable(False, False)

        #Create labels and text input boxes for username and password
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
        self.reg_button = Button(text="Registrate", font=FONT, width=7)


        self.mainloop()

    def login_push(self):
        pass

    def sign_push(self):
        """sign push button"""
        self.username_label_email.pack(before=self.username_label)
        self.username_entry_email.pack(before=self.username_label)
        self.sign_button.config(state="disabled")
        self.reg_button.pack(after=self.sign_button)



login= Login()

