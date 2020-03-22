#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 13:25:56 2020

@author: abhinav
"""


import pygame
from pygame.sprite import Sprite
class Bullet(Sprite):
        """A class to manage bullets fired from the ship"""
        def __init__(self, ai_game):
              """Create a bullet object at the ship's current position."""
              super().__init__()
              self.screen = ai_game.screen
              self.settings = ai_game.settings
              self.color = self.settings.bullet_color
              """
              self.rect=pygame.draw.circle(0, 0, self.settings.bullet_width,self.settings.bullet_height)
              """
              self.rect=pygame.Rect(0, 0, self.settings.bullet_width,self.settings.bullet_height)
              self.rect.midtop = ai_game.ship.rect.midtop
              self.y = float(self.rect.y)
        
        def update(self):
           self.y -= self.settings.bullet_speed
           self.rect.y = self.y
       
        def draw_bullet(self):
           pygame.draw.circle(self.screen,self.color,self.rect.midtop,6)
           