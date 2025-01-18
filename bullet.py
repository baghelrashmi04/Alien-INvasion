import pygame
from pygame.sprite import Sprite

class bullet(Sprite):
    
    def __init__(self,ai_game):
        """create a bullrt object at the ships current position
        """
        super().__init__()
        self.screen = ai_game.screen
        self.setting = ai_game.setting
        self.color = self.setting.bullet_color
        
        """creating a bullet rect at (0,0) and then setting position
        """
        self.rect = pygame.Rect(0,0,self.setting.bullet_width,self.setting.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop
        
        self.y = float(self.rect.y)
        
    def update(self):
        """moving the ship up the screen
        """
        self.y -= self.setting.bullet_speed
        self.rect.y = self.setting.bullet_speed
        self.rect.y = self.y
    def draw_bullet(self):
        """
        Draws the bullet on the screen.

        This method uses the pygame library to draw a rectangle representing
        the bullet on the screen with the specified color and dimensions.

        Args:
            None

        Returns:
            None
        """
        pygame.draw.rect(self.screen,self.color,self.rect)
        
        
        
        
        
        