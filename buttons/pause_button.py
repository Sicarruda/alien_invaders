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

    def _prep_msg(self, msg):
        # Turn msg into a rendered image and center text on the button.
        self.msg_image = self.font.render(msg, True, self.text_color,self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center