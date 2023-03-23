




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
        score_m= self.high_score
        print("!!!!!", score_m)


