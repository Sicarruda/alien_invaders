import sys
import pygame

from settings import Settings
from ship import Ship


class AlienInvasion:
    # Overall class to manage game assets and behavior.

    def __init__(self):
        # Initialize the game, and create game resources.
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )

        pygame.display.set_caption("Attack Invasion")

        self.ship = Ship(self)
        
        # Set the background color.
        # self.bg_color = (150, 150, 150)

    def _check_events(self):
        # Respond to keypresses and mouse events.

        for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    sys.exit()

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
            self._update_screen()
            self.clock.tick(60)


if __name__ == "__main__":
    # Make a game intance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
