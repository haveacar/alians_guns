# constans
SQL_HOST = "sql7.freesqldatabase.com"
DATABASE_USER = "sql7606287"
DATABASE_PASSWORD = "kGMMHFUyl6"
DATABASE_NAME = "sql7606287"
TABLE_NAME = 'game'

import mysql.connector


class Stats:
    """Static events"""

    def __init__(self, max_score, mail):
        # int statistic
        self.reset_stats()
        self.run_game = True
        self.high_score = max_score  # high score game
        self.user_mail = mail

    def reset_stats(self):
        """stats change"""
        self.ships_left = 2
        self.score = 0  # round score

    def update_sql(self):
        with mysql.connector.connect(host=SQL_HOST,
                                     user=DATABASE_USER,
                                     password=DATABASE_PASSWORD,
                                     database=DATABASE_NAME
                                     ) as con:
            # cursor object
            cursor = con.cursor()
            # execute query
            cursor.execute("UPDATE game SET score = %s WHERE email = %s", (self.high_score, self.user_mail))
