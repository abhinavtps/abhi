#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 17:33:41 2020

@author: abhinav
"""
import pygame.font
 
class Button:
    def __init__(self,ai_game,msg):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        self.width, self.height = 100, 50
        self.button_color = ai_game.bg_color
        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont(None, 48)
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.topleft = self.screen_rect.topleft
        self._prep_msg(msg)
    def _prep_msg(self, msg):

       self.msg_image = self.font.render(msg, True, self.text_color,self.button_color)
       self.msg_image_rect = self.msg_image.get_rect()
       self.msg_image_rect.center = self.rect.center
   
    def draw_button(self):

       self.screen.fill(self.button_color, self.rect)
       self.screen.blit(self.msg_image, self.msg_image_rect)
