import pygame
import random
from pygame.sprite import Sprite

class Alian(Sprite):
    """a class presenting a single alian in the fleet
    """
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.setting = ai_game.setting
        self.image = pygame.image.load('alien.bmp')
        self.rect = self.image.get_rect()
        
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
    
    def update(self):
        directions = ['left','rightt','up','down']
        directions = random.choice(directions)
        if directions == 'left':
            self.x -= self.setting.alian_speed
        elif directions == 'right':
            self.x += self.setting.alian_speed
        elif directions =='up':
            self.y -= self.setting.alian_speed
        elif directions == 'down':
            self.y += self.setting.alian_speed
        self.rect.x = self.x
        self.rect.y = self.y
        
        
        
    def check_edges(self):
        """return true if alian is hitting the edge
        """
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <=0:
            return True
        
        
    
            