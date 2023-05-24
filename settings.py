class Settings:
    """Class that stores game settings."""

    def __init__(self):
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed = 1.5
        self.ship_limit = 3

        # Alien settings
        self.alien_speed = 0.25
        self.fleet_drop_speed = 10
        self.fleet_direction = 1  # 1 = right, -1 = left

        # Bullet settings
        self.bullet_speed = 1.5
        self.bullet_width = 4
        self.bullet_height = 15
        self.bullet_color = (70, 70, 70)
        self.bullets_allowed = 3
