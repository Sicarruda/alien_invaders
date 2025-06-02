import pygame

from buttons.button import Button


class BackButton(Button):
    def __init__(self, ai_game, msg):
        super().__init__(ai_game, msg)

        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.rect = pygame.Rect(0, 0, self.width, self.height)

        self._prep_msg(msg)
