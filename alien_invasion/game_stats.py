class GameStats:
    """Track statistics for Alien Invasion"""

    def __init__(self, ai_game):
        """Init stats"""
        self.settings = ai_game.settings
        self.reset_stats()
        # start game in an inactive state
        self.game_active = False
        self.high_score = 0

    def reset_stats(self):
        """Init stats that can change during the game"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
