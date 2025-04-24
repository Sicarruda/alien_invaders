import pygame

from menus.menu import Menu
from buttons.button import Button
from buttons.settings_button import Settings_button

class Initial_menu (Menu):
    def __init__(self, ai_game):
        super().__init__(ai_game)

        # Build the button's rect object.
        self.play_button = Button(self, "PLAY")
        self.settings_button = Settings_button(self, "SETTINGS")
        self.quit_button = Button(self, "QUIT")

        self.list_buttons = [self.play_button, self.settings_button, self.quit_button]

        # Position the buttons in the center of the screen
        self._position_buttons(self.list_buttons)

   