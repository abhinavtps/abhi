#!/usr/bin/env python3 
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 11:32:59 2020

@author: abhinav
"""
import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from time import sleep
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
import pygame.font
class AlienInvasion :
    def __init__(self):
        pygame.init()
        self.settings=Settings()
        self.display_ships=False
        """
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        """
        self.screen=pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.settings.screen_height=self.screen.get_rect().height
        self.settings.screen_width=self.screen.get_rect().width
    
        self.font = pygame.font.SysFont(None, 70)
        self.font1 = pygame.font.SysFont(None, 32)
        self.bg_color = self.settings.bg_color
        self.ship=Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens=pygame.sprite.Group()
        self._create_fleet()
        self.play_button=Button(self,"Play")
        self.stats=GameStats(self)
        self.sb=Scoreboard(self)
        self.screen_rect = self.screen.get_rect()
        self.game_over = self.font.render("GAME OVER ", True,(30,30,30), (72, 211, 216))
        self.play_again=self.font1.render("Click on Play",True,(30,30,30), (72, 211, 216))
        self.game_over_rect = self.game_over.get_rect()
        self.play_again_rect=self.play_again.get_rect()
        self.game_over_rect.center = self.screen_rect.center
        self.play_again_rect.top=self.game_over_rect.bottom
        self.play_again_rect.x=self.game_over_rect.x+80
       
        pygame.display.set_caption("Alien Invasion-@bh!")
    
    
    def _check_keydown_events(self,event):
        if event.key == pygame.K_q:
            self.running=False
        elif event.key== pygame.K_RIGHT:
            self.ship.moving_right=True
        elif event.key== pygame.K_LEFT:
            self.ship.moving_left=True
        elif event.key== pygame.K_UP:
            self.ship.moving_up=True
        elif event.key== pygame.K_DOWN:
            self.ship.moving_down=True
        elif event.key==pygame.K_SPACE:
            self._fire_bullet()
    
    
    def _check_keyup_events(self,event) :
         if event.key== pygame.K_RIGHT:
             self.ship.moving_right=False
         elif event.key== pygame.K_LEFT:
             self.ship.moving_left=False
         elif event.key== pygame.K_UP:
             self.ship.moving_up=False
         elif event.key== pygame.K_DOWN:
             self.ship.moving_down=False
        
    def _check_events(self):
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                self.running=False
            elif event.type == pygame.MOUSEBUTTONDOWN :
                mouse_pos=pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
                
            
            elif event.type== pygame.KEYUP:
                self._check_keyup_events(event)
    
    def _check_play_button(self,mouse_pos):
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
          
        if button_clicked and not self.stats.game_active:
             self.settings.initialize_dynamic_settings()
             self.stats.reset_stats()
             self.sb.prep_score()
             self.sb.prep_level()
             self.sb.prep_ships()
             self.stats.game_active = True
             self.aliens.empty()
             self.bullets.empty()
             self._create_fleet()
             self.ship.center_ship()
             
             
             
             
             
             
             
    
    def _fire_bullet(self):
        new_bullet=Bullet(self)
        self.bullets.add(new_bullet)
    
    
    
    def _update_screen(self):
        self.screen.fill(self.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites() :
            bullet.draw_bullet()
        
        self.aliens.draw(self.screen)
        self.sb.show_score()
        self.play_button.draw_button()
        if self.stats.game_active==False:
           self.screen.blit(self.game_over, self.game_over_rect)
           self.screen.blit(self.play_again,self.play_again_rect)
        pygame.display.flip()
        
        
    def _update_bullets(self) :
        self.bullets.update()
        for bullet in self.bullets.copy():
              if bullet.rect.bottom <=0 :
                  self.bullets.remove(bullet)
        
        self.check_bullet_alien_collision()
        
        
    def check_bullet_alien_collision(self): 
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()
        if not self.aliens:
              self.bullets.empty()
              self._create_fleet()  
              self.settings.increase_speed()
              self.stats.level += 1
              self.sb.prep_level()
        
        
        
    def _create_fleet(self):
        alien=Alien(self)
        self.aliens.add(alien)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)
        
        ship_height=self.ship.rect.height
        available_space_y = (self.settings.screen_height -(3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)
        for row_number in range(number_rows-1):
            for alien_number in range(number_aliens_x+1):
               self._create_alien(alien_number,row_number)
    

    def _create_alien(self,alien_number,row_number):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    
    def _update_aliens(self):
        self._check_fleet_edges()
        self.aliens.update()
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
             self._ship_hit()
        self._check_aliens_bottom()
        
        
    
    def _check_fleet_edges(self):

         for alien in self.aliens.sprites():
             if alien.check_edges():
                 self._change_fleet_direction()
                 break
             
                
     
    def _ship_hit(self):
        if self.stats.ships_left>0:
            self.stats.ships_left-=1
            self.sb.prep_ships()
            self.aliens.empty()
            self.bullets.empty()
            self._create_fleet()
            self.ship.center_ship()
            sleep(0.5)
        
        
        else:
             self.stats.game_active = False
            
            
     
            
            
            
        
        
        
    
    
   
    
    def _check_aliens_bottom(self):
         screen_rect = self.screen.get_rect()
         for alien in self.aliens.sprites():
               if alien.rect.bottom >= screen_rect.bottom:
                   self._ship_hit()
                   break                      
    
    
    def _change_fleet_direction(self):

         for alien in self.aliens.sprites():
               alien.rect.y += self.settings.fleet_drop_speed
         self.settings.fleet_direction *= -1
    
    def run_game(self):
        self.running=True
        while self.running:
          self._check_events()
          if self.stats.game_active :
                  self.ship.update()
                  self._update_bullets()
                  self._update_aliens()
          self._update_screen()
          
        pygame.quit()
        sys.exit()
         

if __name__ == '__main__':
# Make a game instance, and run the game.
   ai = AlienInvasion()
   ai.run_game() 
   
