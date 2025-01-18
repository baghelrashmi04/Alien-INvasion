import sys
from time import sleep
import pygame
from setting import setting
from ship import ship
from bullet import bullet
from alian import Alian
from game_stats import Game_stats
from button import Button
from scoreboard import Scoreboard


class alian_invasion:
    """this is an overall class to manage the assets and behavior
    """
    def __init__(self):
        """initialise the game and create game resources
        """
        pygame.init()
        self.setting = setting()
        
        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.setting.screen_height = self.screen.get_rect().height
        self.setting.screen_width = self.screen.get_rect().width
        pygame.display.set_caption("Alian Invasion")
        self.stats = Game_stats(self)
        self.sb = Scoreboard(self)
        
        """setting the background color
        """
        self.bg_color = (230,230,230)
        self.ship = ship(self)
        self.bullets = pygame.sprite.Group()
        self.alians = pygame.sprite.Group()
        self._create_fleet()
        self.play_button = Button(self,"Play")
               
        
        
    def run_game(self):
        """starting the main loop for the game
        """
        while True:
            self._check_events()
            if self.stats.game_active:
                
               self.ship.update()
               self.update_bullets()
               self.update_alians()
            self._update_screen()
            
            
    def update_bullets(self):
        """updating positions of the bullets and get rid of the old bullets
        """
        self.bullets.update()
            ##getting rid of the bullets that have dissappered
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        self.alian_bullets_collision()
        
        
    def alian_bullets_collision(self):
        collisions = pygame.sprite.groupcollide(self.bullets,self.alians,True,True)
        if collisions:
            for alia in collisions.values():
              self.stats.score += self.setting.alian_scorepoints *len(alia)
            self.sb.prep_score()
            self.sb.check_high_score()
        if not self.alians:
            self.bullets.empty()
            self._create_fleet()
            self.setting.increase_speed()
            self.sb.check_high_score()
            #increase level
            self.stats.level += 1
            self.sb.prep_level()
            
    def check_alians_bottom(self):
        screen_rect = self.screen.get_rect()
        for al in self.alians.sprites():
            if al.rect.bottom >= screen_rect.bottom:
                self.ship_hit()
                break
        
    def check_play_button(self,mouse_pos):
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            self.setting.initialize_dynamic_setting()
            self.stats.game_active = True
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_ships()
            
            self.alians.empty()
            self.bullets.empty()
            
            #create a new fleet and center the ship
            self._create_fleet()
            self.ship.center_ship()
            pygame.mouse.set_visible(False)
        
                        
            
    def _check_events(self):
            ##watch the keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup(event)
            elif event.type == pygame.MOUSEBUTTONUP:
                mouse_pos = pygame.mouse.get_pos()
                self.check_play_button(mouse_pos)
                    
                    
                    
                    
    def _check_keydown(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self.fire_bullet()
        
                    
                    
                        
                        
                        
    def _check_keyup(self,event):    
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
            
            
    def fire_bullet(self):
        """create a new bullet and add it to the bullets group
        """
        if len(self.bullets) < self.setting.bullet_allowed:
           new_bullet = bullet(self)
           self.bullets.add(new_bullet)
           
    
    def _create_fleet(self):
        alian = Alian(self)
        alian_width,alian_height = alian.rect.size
        available_space_x = self.setting.screen_width - (2 * alian_width)
        number_alians_x = available_space_x // (2 * alian_width)
        
    #determinig the number of alians can fit into the screen
        ship_height = self.ship.rect.height
        available_space_y = (self.setting.screen_height - (3* alian_height) - ship_height)
        number_rows = available_space_y // (2* alian_height)
        
        for rows in range(number_rows):
            for alian_number in range(number_alians_x):
                self._create_alian(alian_number,rows)
            
    def _create_alian(self,alian_number,rows):
        alian = Alian(self)
        alian_width,alian_height = alian.rect.size
        alian.x = alian_width + 2 * alian_width * alian_number
        alian.rect.x = alian.x
        alian.rect.y = alian.rect.height + 2 * alian.rect.height * rows 
        self.alians.add(alian)
        
    def check_edges_fleets(self):
        for ali in self.alians.sprites():
            if ali.check_edges():
                self.change_fleet_direction()
                break
            
    def change_fleet_direction(self):
        for ali in self.alians.sprites():
            ali.rect.y += self.setting.fleet_drop_speed
        self.setting.fleet_direction *= -1   
        
    def ship_hit(self):
        #decreament ship left
        if self.stats.ship_left >0:
            #decrement ship hit and update scoreboard
            
            self.stats.ship_left -= 1
            self.sb.prep_ships()
        #get rid of any alians and bullets
            self.bullets.empty()
            self.alians.empty()
        #create a new fleet and center the ship
            self._create_fleet()
            self.ship.center_ship()
            sleep(0.5)
        else:
            self.game_active = False
            pygame.mouse.set_visible(True)
    
        
        
        
        
        
        
    def update_alians(self):
        self.alians.update()
        
        self.check_edges_fleets()    
        if pygame.sprite.spritecollideany(self.ship,self.alians):
            self.ship_hit()
        self.check_alians_bottom()
        
        
                                               
    def _update_screen(self):
        """update the immage on screen and flip the new screen"""              
        ##redraw the screen during each pass through the loop
        self.screen.fill(self.bg_color)
        self.ship.blitme()   
        for bullets in self.bullets.sprites():
            bullets.draw_bullet() 
        self.alians.draw(self.screen)  
        self.sb.show_score()
        if not self.stats.game_active:
            self.play_button.draw_button()  
            ##make the most recently drawn screen visible
        pygame.display.flip()
            
if __name__ == "__main__":
    ##make a game instance and run the game
    ai = alian_invasion()
    ai.run_game()
#collision = alian_invasion()
#collision.update_bullets()       
