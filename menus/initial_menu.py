import pygame

from menus.menu import Menu
from settings import Settings
from buttons.button import Button

class Initial_menu (Menu):
    def __init__(self, ai_game):
        super().__init__(ai_game)

        self.settings = Settings()
        self.width, self.height = 200, 800
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # Build the button's rect object.
        self.play_button = Button(self, "PLAY")
        self.settings_button = Button(self, "SETTINGS")
        self.quit_button = Button(self, "QUIT")

        self.list_buttons = [self.play_button, self.settings_button, self.quit_button]

        # Position the buttons in the center of the screen
        self._position_buttons(self.list_buttons)

   