class Settings:
    """Class that stores game settings."""

    def __init__(self):
        """Initialize the game's STATIC settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed = 1.5
        self.ship_limit = 3

        # Alien settings
        self.fleet_drop_speed = 10

        # Bullet settings
        self.bullet_width = 4
        self.bullet_height = 15
        self.bullet_color = (70, 70, 70)
        self.bullets_allowed = 3

        # Game speed scaling (per level)
        self.speedup_scale = 1.1
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

        #Scoring
        self.alien_points = 50

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed = 1.5
        self.bullet_speed = 1.5
        self.alien_speed = 0.25

        self.fleet_direction = 1  # 1 = right, -1 = left

    def increase_speed(self):
        """Increases game speed."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
