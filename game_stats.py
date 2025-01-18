class Game_stats:
    def __init__(self,ai_game):
        self.setting = ai_game.setting
        self.reset_stats()
        self.high_score = 0
    def reset_stats(self):
        self.ship_left = self.setting.ship_limit
        self.score = 0
        self.level = 1
        
        self.game_active = False