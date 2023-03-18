class Stats():
    """Static events"""
    def __init__(self):
        # int statistic
        self.reset_stats()
        self.run_game = True
        self.high_score = 0

    def reset_stats(self):
        """stats change"""
        self.ships_left = 2
        self.score = 0



