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

    def check_button(self, mouse_pos, pause, restart_key, msg):
        # Pouse the game when the player clicks "PAUSE"
        button_clicked = self.rect.collidepoint(mouse_pos)

        if (button_clicked and msg == "PAUSE") or restart_key:
            pause = not pause
            restart_key = False

        return [pause, restart_key]