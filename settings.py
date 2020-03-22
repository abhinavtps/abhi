#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 15:58:17 2020

@author: abhinav
"""

class Settings:
    def __init__(self) :
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (72, 211, 216)
        #Ship Settings
        
        self.ship_limit=2
        
        #Bullet Settings
        
        self.bullet_width = 6
        self.bullet_height = 10
        self.bullet_color = (255,255, 0)
        
        #Score Setting
        self.alien_points=50
        self.alien_score_scale=1.5
        
        #Alien Setting
       
        self.fleet_drop_speed = 10
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
        
        self.speedup_scale = 1.5
        self.initialize_dynamic_settings()
    
    def initialize_dynamic_settings(self):
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0

        self.fleet_direction = 1
    
    def increase_speed(self):

        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points=int(self.alien_points*self.speedup_scale)

        
        
        
        
        
        
        