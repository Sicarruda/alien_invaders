import sys
import pygame

from settings import Settings
from ship import Ship


class AlienInvasion:
    # Overall class to manage game assets and behavior.

    def __init__(self):
        # Initialize the game, and create game resources.

        pygame.init()

        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        self.ship = Ship(self)

        pygame.display.set_caption("Attack Invasion")

    def _check_events(self):
        # Respond to keypresses and mouse events.

        for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_RIGHT:
                        # Move the ship to the right 
                        self.ship.moving_right = True

                    if event.key == pygame.K_LEFT:
                        # Move the ship to the left.
                        self.ship.moving_left = True
                    
                    if event.key == pygame.K_UP:
                        # Move the ship to the left.
                        self.ship.moving_up = True

                    if event.key == pygame.K_DOWN:
                        # Move the ship to the left.
                        self.ship.moving_down = True

                elif event.type == pygame.KEYUP:

                    if event.key == pygame.K_RIGHT:
                        # Move the ship to the right 
                        self.ship.moving_right = False

                    if event.key == pygame.K_LEFT:
                        # Move the ship to the left.
                        self.ship.moving_left = False
                    
                    if event.key == pygame.K_UP:
                        # Move the ship to the left.
                        self.ship.moving_up = False

                    if event.key == pygame.K_DOWN:
                        # Move the ship to the left.
                        self.ship.moving_down = False
                    

    def _update_screen(self):
        # Update images on the screen, and flip to the new screen.

        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        pygame.display.flip()

    def run_game(self):
        # Start the main loop for the game.

        while True:
            # Watch for keyboard and mouse events.
            self._check_events()
            self.ship.update()
            self._update_screen()
            self.clock.tick(60)


if __name__ == "__main__":
    # Make a game intance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
