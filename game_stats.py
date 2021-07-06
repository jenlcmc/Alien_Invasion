class GameStats:
    """Track statistics for game"""

    def __init__(self, ai_game):
        """Init statistics"""
        self.settings = ai_game.settings
        self.reset_stats()

        #start game in active state
        self.game_active = True
    
    def reset_stats(self):
        """Init stats that can change during game loop"""
        self.ships_left = self.settings.ship_limit