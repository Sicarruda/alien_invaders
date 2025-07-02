class GameStats:
    # Track statistics for the game.

    def __init__(self, ai_game):
        # Initialize statistics.

        self.settings = ai_game.settings
        self.reset_stats()
        self.level = 1

        # High score should never be reset.
        self.high_score = 0
        self.score = 0

        self.lives = ai_game.settings.ship_limit
        self.game_over = False

    def reset_stats(self):
        # Initialize statistics that can change during the game.
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
