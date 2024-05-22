import pygame
import sys
from plane_sprites import *

class Scoreboard:
    def __init__(self, screen, initial_score=0, font_size=36, font_color=(0, 0, 0)):
        self.screen = screen
        self.score = initial_score
        self.font = pygame.font.Font(None, font_size)
        self.font_color = font_color
        self.text = self.font.render('Score: ' + str(self.score), True, self.font_color)
        self.text_rect = self.text.get_rect(topleft=(10, 10))
        self.text_explain=self.font.render('Score greater than 50 to win the game!', True, self.font_color)
        self.text_explain_rect=self.text_explain.get_rect(topleft=(10, 50))

    def update_score(self, points):
        self.score += points
        self.text = self.font.render('Score: ' + str(self.score), True, self.font_color)

    def show_score(self):
        self.screen.blit(self.text, self.text_rect)
        self.screen.blit(self.text_explain, self.text_explain_rect)

class HealthUI:
    def __init__(self, screen, player):
        self.screen = screen
        self.player = player
        self.font = pygame.font.Font(None, 36)  # 设置字体和字号

    def show_health(self):
        health_text = f"Player Health: {self.player.health}"  # 获取玩家当前血量信息
        text_surface = self.font.render(health_text, True, (0, 0, 0))  # 创建文本表面
        text_rect = text_surface.get_rect()
        text_rect.topright = (self.screen.get_width() - 20, 20)  # 设置文本位置为屏幕右上角
        self.screen.blit(text_surface, text_rect)  # 在屏幕上绘制血量信息文本
class BossHealthUI:
    def __init__(self, screen, boss):
        self.healthBG=pygame.image.load('./Pictures/UI/血条2倍.png')
        self.healthBar_Full=pygame.image.load('./Pictures/UI/血条绿.png')
        self.healthBar=self.healthBar_Full
        self.screen = screen
        self.boss = boss
        #设置两个图片的位置在屏幕正上方
        self.healthBG_rect=self.healthBG.get_rect(center=(self.screen.get_width()/2,30))
        self.healthBar_rect=self.healthBar.get_rect(center=(self.screen.get_width()/2,30))

        self.screen = screen
        self.boss = boss
    def draw(self):
        percent=self.boss.health/self.boss.maxhealth
        #根据boss血量裁剪血条
        crop_rect=pygame.Rect(0,0,percent*268,40)
        self.healthBar=self.healthBar_Full.subsurface(crop_rect)
        #显示boss血量
        self.screen.blit(self.healthBG,self.healthBG_rect)
        self.screen.blit(self.healthBar,self.healthBar_rect)
