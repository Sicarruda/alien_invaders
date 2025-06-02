import pygame

from menus.menu import Menu
from buttons.continue_button import ContinueButton
from buttons.play_button import NewGameButton
from buttons.quit_button import QuitButton
from buttons.settings_button import SettingsButton


class InitialMenu(Menu):
    def __init__(self, ai_game):
        super().__init__(ai_game)

        # Build the button's rect object.
        self.active = True
        self.new_game_button = NewGameButton(self, "NEW GAME")
        self.save_button = ContinueButton(self, "CONTINUE")
        self.settings_button = SettingsButton(self, "SETTINGS")
        self.quit_button = QuitButton(self, "QUIT")

        self.list_buttons = [self.new_game_button, self.save_button, self.settings_button, self.quit_button]

        # Position the buttons in the center of the screen
        self.position_buttons(self.list_buttons)
