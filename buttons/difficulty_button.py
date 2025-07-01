import pygame

from buttons.button import Button


class DifficultyButton(Button):
    def __init__(self, ai_game, msg):
        super().__init__(ai_game, msg)

        self.screen = ai_game.screen
        self.settings = ai_game.settings

        self.screen_rect = self.screen.get_rect()
        self.rect = pygame.Rect(0, 0, self.width, self.height)

        self.difficulties = ["easy", "medium", "hard"]
        self.current_index = self.difficulties.index(self.settings.difficulty)

        self._prep_msg(self._get_label())

    # Ajust the label based on the current difficulty
    def _get_label(self):
        return self.difficulties[self.current_index].upper()

    # Change the difficulty to the next one in the list
    def toggle_difficulty(self):
        self.current_index = (self.current_index + 1) % len(self.difficulties)
        self.settings.difficulty = self.difficulties[self.current_index]
        self.settings.game_difficulty()
        self._prep_msg(self._get_label())
