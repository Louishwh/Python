
import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	""" Bullet """
	def __init__(self, setting,screen,ship):
		super(Bullet, self).__init__()
		self.screen = screen

		# 创建一颗子弹
		self.rect = pygame.Rect(0,0,setting.bullet_width,setting.bullet_height)
		self.rect.centerx = ship.rect.centerx
		self.rect.top = ship.rect.top
		
		# 存储 子弹的位置
		self.y = float(self.rect.y)

		self.color = setting.bullet_color
		self.speed_factor = setting.bullet_speed_acter

	def update(self):
		self.y -= self.y

		self.rect.y = self.y


	def drew_bullet(self):
		pygame.draw.rect(self.screen,self.color,self.rect)
		