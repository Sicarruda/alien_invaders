import pygame

from settings import Settings
from button import Button

class Menu ():
    def __init__(self, ai_game):
        super().__init__()

        self.settings = Settings()
        self.width, self.height = 200, 800
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # Build the button's rect object and center it.
        self.rect = pygame.Rect(0,0,self.width,self.height)
        self.rect.center = self.screen_rect.center

        self.play_button = Button(self, "PLAY")
        self.settings_button = Button(self, "SETTINGS")
        self.quit_button = Button(self, "QUIT")

        self.list_buttons = [self.play_button, self.settings_button, self.quit_button]
        self._position_buttons()

    def _position_buttons(self):
        # Espaçamento entre os botões
        spacing = 40
        button_height = self.play_button.rect.height
        total_height = len(self.list_buttons) * button_height + (len(self.list_buttons) - 1) * spacing
        start_y = self.screen_rect.centery - total_height // 2

        for index, button in enumerate(self.list_buttons):
            button.rect.centerx = self.screen_rect.centerx
            button.rect.top = start_y + index * (button_height + spacing)
            button.msg_image_rect.center = button.rect.center  # Alinha o texto com o botão

    def draw_menu(self):
        # Draw blank menu and then draw message.
        for button in self.list_buttons:   
            self.screen.fill(button.button_color, button.rect)
            self.screen.blit(button.msg_image, button.msg_image_rect)