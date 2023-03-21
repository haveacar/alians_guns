class Stats:
    """Static events"""
    def __init__(self, max_score):
        # int statistic
        self.reset_stats()
        self.run_game = True
        self.high_score = max_score # high score game

    def reset_stats(self):
        """stats change"""
        self.ships_left = 2
        self.score = 0  # round score



