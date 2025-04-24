import pygame.font

from buttons.button import Button


class Pause_button(Button):

    def __init__(self, ai_game, msg):
        super().__init__(ai_game, msg,)

        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        self.width, self.height = 100, 30

        self.rect = pygame.Rect(0,0,self.width,self.height)
        self.rect.topright = self.screen_rect.topright

        self.font = pygame.font.SysFont(None, 25)

        self._prep_msg(msg)