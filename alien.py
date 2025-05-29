import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    # A class to represent a single alien in the fleet.

    def __init__(self, ai_game):
        # Initialize the Alien and set its starting position.
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        self.speed = 1.0

        # Load the alien image and set its react.
        self.image = pygame.image.load("images\PNG\playerShip1_blue.png")
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store a float for the alien's exact horizoltal position.
        self.x = float(self.rect.x)


    def check_edges(self):
        # Return True if alien is at edge of screen.
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)

    def update(self):
        # Update the alien's position to left or rigth.

        # Update the screen 
        self.screen_rect = self.screen.get_rect()

        self.x += self.speed * self.settings.fleet_direction
        self.rect.x = self.x

    def restart(self):
        # Reset the ship to the starting position.
        self.screen_rect = self.screen.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

        self.x = self.rect.x
        self.y = self.rect.y

    def blitme(self):
        # Draw the ship at its current location.
        self.screen.blit(self.image, self.rect)

    def level_updade(self):
        self.speed = self.settings.level_up(self.speed)
        return self.speed 
