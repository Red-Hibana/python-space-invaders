import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """Class managing bullets fired from ship"""

    def __init__(self, ai_game):
        """Initialize bullet at ship's position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Create bullet rect at (0,0) then set correct pos
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # Store bullet's firing pos
        self.y = float(self.rect.y)

    def update(self):
        # Move bullet upscreen
        self.y -= self.settings.bullet_speed
        # Update rect with movement
        self.rect.y = self.y

    def draw_bullet(self):
        """Draws bullet to screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
