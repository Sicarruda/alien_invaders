import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    # A class to represent a single alien in the fleet.

    def __init__(self, ai_game):
        # Initialize the Alien and set its starting position.
        super().__init__()
        self.screen = ai_game.screen

        # Load the alien image and set its react.
        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store a float for the alien's exact horizoltal position.
        self.x = float(self.rect.x)

    def update(self):
        # Update the ship's position based on the movement flags.
        self.screen_rect = self.screen.get_rect()
        # Update the ship's x value, not the rect.

        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed

        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        if self.moving_bottom and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed

        if self.moving_top and self.rect.top > 0:
            self.y -= self.settings.ship_speed

        # Update rect object from self.x and self.y.
        self.rect.x = self.x
        self.rect.y = self.y

    def restart(self):
        # Reset the ship to the starting position.
        self.screen_rect = self.screen.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

        self.x = self.rect.x
        self.y = self.rect.y

    def blitme(self):
        # Draw the ship at its current location.

        self.screen.blit(self.image, self.rect)
