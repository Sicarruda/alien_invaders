import pygame

from settings import Settings

class Menu():
    def __init__(self, ai_game):
        self.settings = Settings()
        self.width, self.height = 200, 800
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

    def position_buttons(self, list_buttons):
        # Espaçamento entre os botões
        spacing = 15
        button_height = list_buttons[0].rect.height
        total_height = len(list_buttons) * button_height + (len(list_buttons) - 1) * spacing
        start_y = self.screen_rect.centery - total_height // 2

        for index, button in enumerate(list_buttons):
            button.rect.centerx = self.screen_rect.centerx
            button.rect.top = start_y + index * (button_height + spacing)
            button.msg_image_rect.center = button.rect.center  # Alinha o texto com o botãoo
    
    def draw_menu(self):
    # Draw blank menu and then draw message.
        for button in self.list_buttons:   
            self.screen.fill(button.button_color, button.rect)
            self.screen.blit(button.msg_image, button.msg_image_rect)
    