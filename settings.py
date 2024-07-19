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

        # Ship settings:
        self.ship_speed = 7

        # Bullet settings:
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 5