import pygame
from pygame.sprite import Sprite

class setting:
    """a class to store all settings of aliean invasion
    """
    def __init__(self):
        """initlise the games settings
        """
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (230,230,230)
        self.ship_limit = 3
        self.bullet_speed = 1.5
        self.bullet_width = 5
        self.bullet_height = 20
        self.bullet_color = (60,60,60)
        self.bullet_allowed = 3
        self.fleet_drop_speed = 10
        
        
        ##how the game speeds up
        self.speedup_scale = 1.1
        self.score_scale = 1.5
        self.initialize_dynamic_setting()
        
    def initialize_dynamic_setting(self):
        self.alian_speed = 1.0
        self.bullet_speed = 3
        self.ship_speed = 1.5
        self .fleet_direction = 1
        self.alian_scorepoints = 50
        
    def increase_speed(self):
        self.alian_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.ship_speed *= self.speedup_scale
        self.alian_scorepoints = int(self.alian_scorepoints * self.score_scale)
        