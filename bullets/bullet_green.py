import pygame

from bullets.bullet import Bullet


class BulletGreen(Bullet):

    def __init__(self, ai_game):
        # Create a bullet object at the ship's current position.

        super().__init__(ai_game)
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = (0,255,0)
        self.bullet_speed = 2.0
        self.bullet_allowed = 10
        self.bullet_dameged = 2
        
        # Create a bullet rect at (0,0) and then set correct position.
        self.rect = pygame.Rect(
            0, 0, self.bullet_width, self.bullet_height
        )
        self.rect.midtop = ai_game.ship.rect.midtop

        # Store the bullet's position as a float.
        self.y = float(self.rect.y)