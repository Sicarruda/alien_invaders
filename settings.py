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
        self.bg_color = (255, 255, 255)
        self.fullscreen_mode = False
        self.background_image = pygame.image.load("images/nightskycolor.bmp")

        # Ship settings:
        self.ship_limit = 2

        # Aliens settings:
        self.fleet_drop_speed = 10
        self.alien_speed = 1.0
        
        # fleet_diretction of 1 = right; -1 = left.
        self.fleet_direction = 1

        # How quickly the game speeds up
        self.speedup_scale = 1.1
        
        # How quickly the alien point values increase
        self.score_scale = 1.1

        # Scoring settings
        self.alien_points = 10

    def level_up(self, object_update):
       object_update *= self.speedup_scale
       return object_update
    
