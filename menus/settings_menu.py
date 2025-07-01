import pygame

from menus.menu import Menu
from buttons.back_button import BackButton
from buttons.difficulty_button import DifficultyButton
from buttons.fullscreen_button import FullscreenButton

class SettingsMenu (Menu):
    def __init__(self, ai_game):
        super().__init__(ai_game)

        # Build the button's rect object.
        self.active = False
        self.difficulty_button = DifficultyButton(self, "")  
        self.fullscreen_button = FullscreenButton(self, "FULLSCREEN OFF")  
        self.back_button = BackButton(self, "BACK")

        self.list_buttons = [self.difficulty_button, self.fullscreen_button, self.back_button]
        
        # Position the buttons in the center of the screen
        self.position_buttons(self.list_buttons)