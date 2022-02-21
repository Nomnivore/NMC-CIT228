class Settings:
    """A class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initialize the game's settings"""
        self.dev_mode = True

        # screen settings
        self.screen_width = 1366
        self.screen_height = 768
        self.bg_color = (230, 230, 230)

        # self.ship_speed = 3.5
        self.ship_limit = 3

        # self.bullet_speed = 2.0
        self.bullet_width = 5
        self.bullet_height = 12
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # self.alien_speed = 1.0
        self.fleet_drop_speed = 10

        # how quickly the game speeds up
        self.speedup_scale = 1.1

        # how quickly the alien point values increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

        if self.dev_mode:
            self.bullets_allowed = 200
            self.bullet_width = 300
            self.fleet_drop_speed = 80

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game"""
        self.ship_speed = 3.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0
        # 1 = right, -1 = left
        self.fleet_direction = 1

        # Scoring
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed settings and alien point values"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
