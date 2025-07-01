import sys
import pygame

from time import sleep

from settings import Settings
from ship import Ship
from bullets.bullet_black import BulletBlack
from bullets.bullet_blue import BulletBlue
from bullets.bullet_green import BulletGreen
from bullets.bullet_red import BulletRed
from alien import Alien
from game_stats import GameStats
from buttons.pause_button import PauseButton
from scoreboard import Scoreboard
from menus.initial_menu import InitialMenu
from menus.settings_menu import SettingsMenu
from game_state_saver import GameStateSaver


class AlienInvasion:
    # Overall class to manage game assets and behavior.

    def __init__(self):
        # Initialize the game, and create game resources.

        pygame.init()

        # Start Alien Invasion in an inactive state.
        self.game_active = False

        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.change_screen_mode = False
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width_standard, self.settings.screen_height_standard)
        )
        self.background_image = self.settings.background_image

        # Menu bar
        self.initial_menu = InitialMenu(self)
        self.settings_menu = SettingsMenu(self)

        # Pause the game
        self.pause_button = PauseButton(self, "PAUSE")
        self.pause = False
        self.restart_key = False

        # Create an instance to store game statistics
        self.stats = GameStats(self)
        self.score = Scoreboard(self)
        self.level_up = False
        self.reset_game = False

        # Create the ship
        self.ship = Ship(self)
        self.ship_restart = False

        # Create the bullets
        self.bullet_tipe = 1  # 1 = black; 2 = red; 3 = green; 4 = blue
        self.bullets_black_group = pygame.sprite.Group()
        self.bullets_red_group = pygame.sprite.Group()
        self.bullets_green_group = pygame.sprite.Group()
        self.bullets_blue_group = pygame.sprite.Group()
        self.bullet_black = BulletBlack(self)
        self.bullet_red = BulletRed(self)
        self.bullet_blue = BulletBlue(self)
        self.bullet_green = BulletGreen(self)

        self.aliens = pygame.sprite.Group()
        self.alien_speed = 1

        # Save the game state
        self.save_game_state = GameStateSaver(self)

        pygame.display.set_caption("Attack Invasion")

    def _create_alien(self, x_position, y_position):
        # Create an alien and place it in the row.

        new_alien = Alien(self)

        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        new_alien.speed = self.alien_speed
        self.aliens.add(new_alien)

    def _create_fleet(self):
        # Create the fleet of aliens
        # TODO ajustar para os 2 modos de exibição de tela
        # Create an alien and keep adding aliens until there's no room left.
        # Spacing between aliens is one alien width and one alien height.

        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        current_x, current_y = alien_width, alien_height

        while current_y < (self.settings.screen_height_standard - 3 * alien_height):
            while current_x < (self.settings.screen_width_standard - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width

            # finished a row; reset x value, and increment y value.
            current_x = alien_width
            current_y += 2 * alien_height

        if self.level_up:
            self.alien_speed += alien.level_updade()
            self.settings.alien_points *= self.settings.score_scale

        self.level_up = False
        self.reset_game = False

    def _check_fleet_edges(self):
        # Respond appropriately if any aliens have reached an edge.

        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        # Drop the entire fleet and change the fleet's direction.

        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed

        self.settings.fleet_direction *= -1

    def _check_keydown_events(self, event):
        # Respond to keypresses.

        if event.key == pygame.K_q:
            # Exit to the game when press q.
            sys.exit()

        if event.key == pygame.K_f:
            # Change the variables to change the screen mode.
            self.change_screen_mode = True
            # self.ship_restart = True

            self.settings.fullscreen_mode = not self.settings.fullscreen_mode

        if event.key == pygame.K_p:
            # key to start and pause the game
            if self.game_active:
                self.restart_key = True
                checked_pause = self.pause_button.check_button(
                    (0, 0), self.pause, self.restart_key, self.pause_button.msg
                )
                self.pause = checked_pause[0]
                self.restart_key = checked_pause[1]

            else:
                if self.stats.ships_left == 0:
                    self.stats.reset_stats()
                    self.alien_speed = 1
                    self.save_game_state.save_to_json()
                else:
                    self.save_game_state.load_from_json()

                self.restart_key = True
                self.ship.reset_update()
                self.score.prep_score()
                self.score.prep_level()
                self.settings.alien_points = 1

                self.reset_game = True
                self.game_active = True
                self.restart_key = False

                # # Get rid of any remaining bullets and aliens and restart de game.
                self.aliens.empty()
                self._restart_fleet()
                self.ship.restart()

                # # Show the mouse cursor.
                pygame.mouse.set_visible(True)

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
            mouse_pos = pygame.mouse.get_pos()

            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.initial_menu.active:
                    if self.initial_menu.new_game_button.check_button(
                        mouse_pos, self.initial_menu.new_game_button.msg
                    ):
                        if self.stats.ships_left == 0:
                            self.stats.reset_stats()
                            self.alien_speed = 1
                            self.save_game_state.save_to_json()
                        else:
                            self.save_game_state.load_from_json()
                        self.ship.reset_update()
                        self.score.prep_score()
                        self.score.prep_level()
                        self.settings.alien_points = 1

                        self.reset_game = True
                        self.game_active = True
                        self.restart_key = False

                        # Get rid of any remaining bullets and aliens and restart de game.
                        self.aliens.empty()
                        self._restart_fleet()
                        self.ship.restart()

                        # Show the mouse cursor.
                        pygame.mouse.set_visible(True)

                    if self.initial_menu.quit_button.check_button(
                        mouse_pos, self.initial_menu.quit_button.msg
                    ):
                        sys.exit()

                    if self.initial_menu.settings_button.check_button(
                        mouse_pos, self.initial_menu.settings_button.msg
                    ):
                        self.settings_menu.active = True
                        self.initial_menu.active = False

                if self.settings_menu.active:
                    if self.settings_menu.back_button.check_button(
                        mouse_pos, self.settings_menu.back_button.msg
                    ):
                        self.settings_menu.active = False
                        self.initial_menu.active = True

                    if self.settings_menu.fullscreen_button.check_button(
                        mouse_pos, self.settings_menu.fullscreen_button.msg
                    ):
                        # Change the variables to change the screen mode.
                        self.settings.fullscreen_mode = not self.settings.fullscreen_mode
                        self.settings_menu.fullscreen_button._prep_msg(
                            "FULLSCREEN ON" if not self.settings.fullscreen_mode else "FULLSCREEN OFF"
                        )

                    if self.settings_menu.difficulty_button.check_button(
                        mouse_pos, self.settings_menu.difficulty_button.msg
                    ):
                        # Change the difficulty of the game.
                        self.settings_menu.difficulty_button.toggle_difficulty()

                checked_pause = self.pause_button.check_button(
                    mouse_pos, self.pause, self.restart_key, self.pause_button.msg
                )
                self.pause = checked_pause[0]
                self.restart_key = checked_pause[1]

    def _fire_bullet(self):
        # Create a new bullet and add it to the bullets group.
        if (
            self.bullet_tipe == 1
            and len(self.bullets_black_group) < self.bullet_black.bullet_allowed
        ):
            new_bullet = BulletBlack(self)
            self.bullets_black_group.add(new_bullet)

        if (
            self.bullet_tipe == 2
            and len(self.bullets_red_group) < self.bullet_red.bullet_allowed
        ):
            new_bullet = BulletRed(self)
            self.bullets_red_group.add(new_bullet)

        if (
            self.bullet_tipe == 3
            and len(self.bullets_green_group) < self.bullet_green.bullet_allowed
        ):
            new_bullet = BulletGreen(self)
            self.bullets_green_group.add(new_bullet)

        if (
            self.bullet_tipe == 4
            and len(self.bullets_blue_group) < self.bullet_blue.bullet_allowed
        ):
            new_bullet = BulletBlue(self)
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
            if bullet.rect.bottom <= 0:
                self.bullets_black_group.remove(bullet)

        for bullet in self.bullets_red_group.copy():
            if bullet.rect.bottom <= 0:
                self.bullets_red_group.remove(bullet)

        for bullet in self.bullets_green_group.copy():
            if bullet.rect.bottom <= 0:
                self.bullets_green_group.remove(bullet)

        for bullet in self.bullets_blue_group.copy():
            if bullet.rect.bottom <= 0:
                self.bullets_blue_group.remove(bullet)

        self._bullet_alien_collisions()

    def _bullet_alien_collisions(self):
        # Check for any bullets that have hit aliens. If so, get rid of the bullet and the alien.

        collision_black_bullet = pygame.sprite.groupcollide(
            self.bullets_black_group, self.aliens, True, True
        )
        collision_red_bullet = pygame.sprite.groupcollide(
            self.bullets_red_group, self.aliens, True, True
        )
        collision_green_bullet = pygame.sprite.groupcollide(
            self.bullets_green_group, self.aliens, True, True
        )
        collision_blue_bullet = pygame.sprite.groupcollide(
            self.bullets_blue_group, self.aliens, True, True
        )

        if (
            collision_black_bullet
            or collision_red_bullet
            or collision_green_bullet
            or collision_blue_bullet
        ):
            self.stats.score = round(self.stats.score + (self.settings.alien_points), 2)
            self.score.prep_score()
            self.score.check_high_score()

        if not self.aliens:
            self.level_up = True
            self._restart_fleet()
            self.ship.level_updade()

            # Increase level.
            self.stats.level += 1
            self.score.prep_level()
            self.save_game_state.save_to_json()

    def _restart_fleet(self):
        # Destroy existing bullets and create new fleet.
        self.bullets_black_group.empty()
        self.bullets_red_group.empty()
        self.bullets_green_group.empty()
        self.bullets_blue_group.empty()
        self._create_fleet()

    def _update_aliens_position(self):
        # Update the position of all aliens in the fleet.

        self._check_fleet_edges()
        self.aliens.update()

        # look for aliens-ship collisions
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # Look for aliens hitting the bottom of the screen.
        self._check_aliens_bottom()

    def _ship_hit(self):
        # Respond to the ship being hit by an alien.

        if self.stats.ships_left > 0:
            # Decrement ships_left
            self.stats.ships_left -= 1

            # Get rid of any remaining bullets and aliens and restart fleet and ship
            self.aliens.empty()
            self._restart_fleet()
            self.ship.restart()

            # Pause.
            sleep(0.5)
        else:
            self.game_active = False
            pygame.mouse.set_visible(True)

    def _check_aliens_bottom(self):
        # Check if any aliens have reached the bottom of the screen.
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height_standard:
                self._ship_hit()
                break

    def _live_draw(self):
        # Draw the number of ships left.
        for ship_number in range(self.stats.ships_left):
            ship_rect = self.ship.life_image.get_rect()
            ship_rect.x = 10 + ship_number * ship_rect.width
            ship_rect.y = 10
            self.screen.blit(self.ship.life_image, ship_rect)

    def _update_screen(self):
        # Update images on the screen, and flip to the new screen.

        self.screen.fill(self.settings.bg_color)
        self.screen.blit(self.background_image, (0, 0))

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

        # Draw the score information
        self.score.show_score()

        self._live_draw()

        # Draw the menus if the game is inactive.
        if not self.game_active and self.initial_menu.active:
            self.initial_menu.draw_menu()
        if not self.game_active and self.settings_menu.active:
            self.settings_menu.draw_menu()

        # Draw the pause button if the game is active.
        if self.game_active:
            self.pause_button.draw_button()

        pygame.display.flip()

    def run_game(self):
        # Start the main loop for the game.

        while True:
            self._check_events()

            if self.game_active and not self.pause:

                self.ship.update_position()
                self._update_bullets()
                self._update_aliens_position()

            self._update_screen()
            self.clock.tick(60)


if __name__ == "__main__":
    # Make a game intance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
