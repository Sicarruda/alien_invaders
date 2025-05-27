import pygame

from menus.menu import Menu
from buttons.button import Button
from buttons.save_button import Save_button
from buttons.play_button import Play_button
from buttons.quit_button import Quit_button
from buttons.settings_button import Settings_button


class Initial_menu(Menu):
    def __init__(self, ai_game):
        super().__init__(ai_game)

        # Build the button's rect object.
        self.play_button = Button(self, "PLAY")
        self.save_button = Play_button(self, "SAVE")
        self.settings_button = Settings_button(self, "SETTINGS")
        self.quit_button = Quit_button(self, "QUIT")

        self.list_buttons = [self.play_button, self.save_button, self.settings_button, self.quit_button]

        # Position the buttons in the center of the screen
        self.position_buttons(self.list_buttons)

    # Check who is the button clicked and return the button clicked
    def check_buttons_click(self, mouse_pos):
        button_clicked = self.rect.collidepoint(mouse_pos)
        for button in self.list_buttons:
            if button.rect.collidepoint(mouse_pos):
                return button.check_button(button_clicked, msg=button.msg)
