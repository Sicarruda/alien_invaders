import sys
import pygame

from settings import Settings
from ship import Ship
from bullet_black import Bullet_black
from bullet_blue import Bullet_blue
from bullet_green import Bullet_green
from bullet_red import Bullet_red
from alien import Alien

class AlienInvasion:
    # Overall class to manage game assets and behavior.

    def __init__(self):
        # Initialize the game, and create game resources.

        pygame.init()

        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.change_screen_mode = False
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width_standard, self.settings.screen_height_standard)
        )

        self.ship = Ship(self)
        self.ship_restart = False

        self.bullet_tipe = 1 # 1 = black; 2 = red; 3 = green; 4 = blue
        self.bullets_black_group = pygame.sprite.Group()
        self.bullets_red_group =pygame.sprite.Group()
        self.bullets_green_group =pygame.sprite.Group()
        self.bullets_blue_group = pygame.sprite.Group()
        self.bullet_black = Bullet_black(self)
        self.bullet_red = Bullet_red(self)
        self.bullet_blue = Bullet_blue(self)
        self.bullet_green = Bullet_green(self)

        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        pygame.display.set_caption("Attack Invasion")

    def _create_fleet(self):
        # Create the fleet of aliens

        # Make an alien.
        alien = Alien(self)
        self.aliens.add(alien)

    def _check_keydown_events(self, event):
        # Respond to keypresses.
        
        if event.key == pygame.K_q:
            # Exit to the game when press q. 
            sys.exit()
        
        if event.key == pygame.K_f:
            # Change the variables to change the screen mode.
            self.change_screen_mode = True
            self.ship_restart = True

            self.settings.fullscreen_mode = not self.settings.fullscreen_mode

        if event.key == pygame.K_RIGHT:
            # Move the ship to the right
            self.ship.moving_right = True

        if event.key == pygame.K_LEFT:
            # Move the ship to the left.
            self.ship.moving_left = True

        if event.key == pygame.K_UP:
            # Move the ship to the top.
            self.ship.moving_top = True

        if event.key == pygame.K_DOWN:
            # Move the ship to the botton.
            self.ship.moving_bottom = True

        if event.key == pygame.K_SPACE:
            # Fire the bullets
            self._fire_bullet()

        if event.key == pygame.K_1:
            # change bullet to bullet_black
            self.bullet_tipe = 1  

        if event.key == pygame.K_2:
            # change bullet to bullet_red
            self.bullet_tipe = 2

        if event.key == pygame.K_3:
            # change bullet to bullet_green
            self.bullet_tipe = 3

        if event.key == pygame.K_4:
            # change bullet to bullet_blue
            self.bullet_tipe = 4

    def _check_keyup_events(self, event):
        # Respond to keypresses.

        if event.key == pygame.K_RIGHT:
            # Move the ship to the right
            self.ship.moving_right = False

        if event.key == pygame.K_LEFT:
            # Move the ship to the left.
            self.ship.moving_left = False

        if event.key == pygame.K_UP:
            # Move the ship to the top.
            self.ship.moving_top = False

        if event.key == pygame.K_DOWN:
            # Move the ship to the botton.
            self.ship.moving_bottom = False

    def _check_events(self):
        # Respond to keypresses and mouse events.

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _fire_bullet(self):
        # Create a new bullet and add it to the bullets group.
        if self.bullet_tipe == 1 and len(self.bullets_black_group) < self.bullet_black.bullet_allowed:
            new_bullet = Bullet_black(self)
            self.bullets_black_group.add(new_bullet)

        if self.bullet_tipe == 2 and len(self.bullets_red_group) < self.bullet_red.bullet_allowed:
            new_bullet = Bullet_red(self)
            self.bullets_red_group.add(new_bullet)

        if self.bullet_tipe == 3 and len(self.bullets_green_group) < self.bullet_green.bullet_allowed:
            new_bullet = Bullet_green(self)
            self.bullets_green_group.add(new_bullet)

        if self.bullet_tipe == 4 and len(self.bullets_blue_group) < self.bullet_blue.bullet_allowed:
            new_bullet = Bullet_blue(self)
            self.bullets_blue_group.add(new_bullet)        

    def _update_bullets(self):
        # Update position of bullets and get rid of old bullets.
        
            # Update bullets position
            self.bullets_black_group.update()
            self.bullets_red_group.update()
            self.bullets_green_group.update()
            self.bullets_blue_group.update()

            # Get rid of bullets that have disappeared.
            for bullet in self.bullets_black_group.copy():
                if bullet.rect.bottom <=0:
                    self.bullets_black_group.remove(bullet)

            for bullet in self.bullets_red_group.copy():
                if bullet.rect.bottom <=0:
                    self.bullets_red_group.remove(bullet)

            for bullet in self.bullets_green_group.copy():
                if bullet.rect.bottom <=0:
                    self.bullets_green_group.remove(bullet)

            for bullet in self.bullets_blue_group.copy():
                if bullet.rect.bottom <=0:
                    self.bullets_blue_group.remove(bullet)

    def _update_screen(self):
        # Update images on the screen, and flip to the new screen.

        self.screen.fill(self.settings.bg_color)
        
        if self.change_screen_mode:
            # Change screen mode to Fullscreen.
            if self.settings.fullscreen_mode:
                self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
                self.settings.screen_width = self.screen.get_rect().width
                self.settings.screen_height = self.screen.get_rect().height
    
                self.change_screen_mode = False

            else:
                # Change screen mode to standart mode.
                self.screen = pygame.display.set_mode(
                    (
                        self.settings.screen_width_standard,
                        self.settings.screen_height_standard,
                    )
                )
                
                self.change_screen_mode = False

        for bullet in self.bullets_black_group.sprites():
            bullet.draw_bullet()

        for bullet in self.bullets_red_group.sprites():
            bullet.draw_bullet()

        for bullet in self.bullets_green_group.sprites():
            bullet.draw_bullet()
                
        for bullet in self.bullets_blue_group.sprites():
            bullet.draw_bullet()

        if self.ship_restart:
            # Restart the ship position
            self.ship.restart()
            self.ship_restart = False

        self.ship.blitme()
        self.aliens.draw(self.screen)
    
        pygame.display.flip()

    def run_game(self):
        # Start the main loop for the game.

        while True:
            # Watch for keyboard and mouse events.
            self._check_events()           
            self.ship.update()
            self._update_bullets()
            self._update_screen()
            self.clock.tick(60)


if __name__ == "__main__":
    # Make a game intance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
