#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 16:40:46 2020

@author: abhinav
"""
class GameStats:
    
    def __init__(self,ai_game):
        self.settings=ai_game.settings
        self.reset_stats()
        self.game_active=False
        self.high_score=0
        
    def reset_stats(self):
        self.ships_left = self.settings.ship_limit
        self.score=0
        self.level=1
