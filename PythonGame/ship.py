import pygame

class Ship(object):
	"""doc string for Ship"""
	def __init__(self,setting,screen):
		self.screen = screen
		self.setting = setting

		#加载图片并获取矩形框
		self.image = pygame.image.load('images/rock.png')
		self.image_rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		#放置矩形
		self.image_rect.centerx = self.screen_rect.centerx
		self.image_rect.bottom = self.screen_rect.bottom

		# 
		self.center = float(self.image_rect.centerx)

		#
		self.moving_right = False
		self.moving_left = False

	def blitme(self):
		""" 在制定位置绘制飞船 """
		self.screen.blit(self.image,self.image_rect)

	def update(self):
		if self.moving_right and self.image_rect.right < self.screen_rect.right:
			self.center += self.setting.ship_speed_facter
		if self.moving_left and self.image_rect.left > 0 :
			self.center -= self.setting.ship_speed_facter 

		# 根据self.center更新 rect 对象
		self.image_rect.centerx = self.center