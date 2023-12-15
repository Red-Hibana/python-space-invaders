import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    """Class for ship."""

    def __init__(self, ai_game):
        super().__init__()
        # Initialize screen/start pos
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load ship image and get rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Start ship at middle bottom
        self.rect.midbottom = self.screen_rect.midbottom

        # Store ship's horizontal pos
        self.x = float(self.rect.x)

        # Movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update ship's position."""
        # Get desired movement (and prevent going off-screen)
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Update rect with movement
        self.rect.x = self.x

    def blitme(self):
        """Draw ship at its current location."""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Puts ship at center of screen."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
