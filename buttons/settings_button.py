import pygame.font

from buttons.button import Button


class Settings_button(Button):

    def __init__(self, ai_game, msg):
        super().__init__(ai_game, msg,)
      
        self._prep_msg(msg)
        

   