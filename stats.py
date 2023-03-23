from database import *
class Stats:
    """Static events"""

    def __init__(self, max_score, mail, name):
        # int statistic
        self.reset_stats()
        self.run_game = True
        self.high_score = max_score  # high score game
        self.user_mail = mail
        self.user_name = name

    def reset_stats(self):
        """stats change"""
        self.ships_left = 2
        self.score = 0  # round score

    def update_sql(self):

        score_m= self.high_score

        # sql request
        request_sql = f"""UPDATE "main"."game" SET "score"={score_m} WHERE "email"='$mail$'"""
        request_sql = request_sql.replace('$mail$', self.user_mail)


        try:
            with sqlite3.connect(DB_URL) as sqlite_connection:  # Connect to database
                # Create cursor object
                cursor = sqlite_connection.cursor()
                # Execute SQL query
                cursor.execute(request_sql)

        except sqlite3.Error as err:
            print("***Sql error***", err, sep="-")

        else:
            print("***Complete***")



