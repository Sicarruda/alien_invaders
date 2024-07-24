import pygame
class Settings:
    # A class to store all settings for Alien Invasion.

    def __init__(self):
        # Initialize the game's settings.

        # Screen settings:
        self.screen_width = 0
        self.screen_height = 0
        self.screen_width_standard = 1200
        self.screen_height_standard = 800
        self.bg_color = (230, 230, 230)
        self.fullscreen_mode = False
        self.background_image = pygame.image.load("images/nightskycolor.bmp")

        # Ship settings:
        self.ship_speed = 7
        self.shep_limit = 3
        
        # Aliens settings:
        self.fleet_drop_speed = 10
        # fleet_diretction of 1 = right; -1 = left.
        self.fleet_direction = 1