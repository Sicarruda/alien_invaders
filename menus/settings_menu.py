import pygame

from menus.menu import Menu
from settings import Settings
from buttons.button import Button

class Settings_menu (Menu):
    def __init__(self, ai_game):
        super().__init__(ai_game)
