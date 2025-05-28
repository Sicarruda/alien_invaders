import json

from game_stats import GameStats

# class to save the game state to a JSON file.
class GameStateSaver:
    def __init__(self, ai_game):

        self.stats = ai_game.stats
        self.settings = ai_game.settings
        # Initialize the state dictionary.      
        self.state = {}
    
    def create_state(self):
        # Create a state dictionary with the current game state.
        self.state = {
            "score": self.stats.score,
            "level": self.stats.level,
            "ships_left": self.stats.ships_left,
            "high_score": self.stats.high_score,
            "settings": {
                "screen_width": self.settings.screen_width,
                "screen_height": self.settings.screen_height,
                "screen_width_standard": self.settings.screen_width_standard,
                "screen_height_standard": self.settings.screen_height_standard,
                "fullscreen_mode": self.settings.fullscreen_mode,
                "bg_color": self.settings.bg_color,
                "ship_limit": self.settings.ship_limit,
                "alien_speed": self.settings.alien_speed,
                "fleet_drop_speed": self.settings.fleet_drop_speed,
                "fleet_direction": self.settings.fleet_direction,
                "difficulty": self.settings.difficulty
            }
        }

    # Save the game state to a JSON file.
    def save_to_json(self, filename="game_state.json"):
        self.create_state()

        with open(filename, "w") as f:
            print(self.state, "saving to file")
            json.dump(self.state, f)
