import json

# class to save the game state to a JSON file.
class GameStateSaver:
    def __init__(self, ai_game):
        self.ai_game = ai_game
        self.stats = ai_game.stats
        self.settings = ai_game.settings
        self.ship = ai_game.ship
        # Initialize the state dictionary.      
        self.state = {}
    
    def create_state(self):
        # Create a state dictionary with the current game state.
        self.state = {
            "score": self.stats.score,
            "level": self.stats.level,
            "ships_left": self.stats.ships_left,
            "high_score": self.stats.high_score,
            "alien_speed": self.ai_game.alien_speed,
            "settings": {
                "screen_width_standard": self.settings.screen_width_standard,
                "screen_height_standard": self.settings.screen_height_standard,
                "fullscreen_mode": self.settings.fullscreen_mode,
                "fleet_drop_speed": self.settings.fleet_drop_speed,
                "fleet_direction": self.settings.fleet_direction,
                "ship_limit": self.settings.ship_limit,
                "difficulty": self.settings.difficulty
            }
        }

    # Save the game state to a JSON file.
    def save_to_json(self, filename="game_state.json"):
        self.create_state()
        with open(filename, "w") as f:
            json.dump(self.state, f)

    def load_from_json(self, filename="game_state.json"):
        try:
            with open(filename, "r") as f:
                self.state = json.load(f)
                
                # Update the game stats and settings with the loaded state.
                self.stats.score = self.state["score"]
                self.stats.level = self.state["level"]
                self.stats.ships_left = self.state["ships_left"]
                self.stats.high_score = self.state["high_score"]
                self.ai_game.alien_speed = self.state["alien_speed"]
                self.settings.screen_width_standard = self.state["settings"]["screen_width_standard"]
                self.settings.screen_height_standard = self.state["settings"]["screen_height_standard"]
                self.settings.fullscreen_mode = self.state["settings"]["fullscreen_mode"]
                self.settings.ship_limit = self.state["settings"]["ship_limit"]
                self.settings.fleet_drop_speed = self.state["settings"]["fleet_drop_speed"]
                self.settings.fleet_direction = self.state["settings"]["fleet_direction"]
                self.settings.difficulty = self.state["settings"]["difficulty"]

        except FileNotFoundError:
            print("No saved game state found.")