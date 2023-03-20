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
        self.geometry("400x200")
        self.resizable(False, False)

        # Create labels and text input boxes for username and password
        username_label = Label(text="Username:")
        username_label.pack()
        username_entry = Entry()
        username_entry.pack()

        password_label = Label(text="Password:")
        password_label.pack()
        password_entry = Entry(show="*")
        password_entry.pack()

        login_button = Button(text="Login", command=self.login_push)
        login_button.pack()

        self.mainloop()

    def login_push(self):
        pass


login= Login()

