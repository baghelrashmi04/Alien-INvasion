import pygame
from pygame.sprite import Sprite

class ship(Sprite):
    def __init__(self,ai_game):
        """initialize the ship and set its starting position
        """
        super().__init__()
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.setting = ai_game.setting
        
        ##load the image of ship and get its rect
        self.image = pygame.image.load('ship.bmp')
        self.rect = self.image.get_rect()
        ##start each new ship at the bottom of the screen
        self.rect.midbottom = self.screen_rect.midbottom
        ##storing a decimal value for the ships horizontal position
        self.x = float(self.rect.x)
        
        self.moving_right = False
        self.moving_left = False
    def update(self):
        """updating ship position based on the movement 
        updating ship value not that of rect
        """
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.setting.ship_speed
        if self.moving_left and self.rect.left> 0:
            self.x -= self.setting.ship_speed
        """updating the rect object from self.x
        """
        self.rect.x = self.x
            
            
    def blitme(self):
        ##draw the ship at its current location
        self.screen.blit(self.image,self.rect)
        
    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        