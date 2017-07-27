import sys

import pygame
from bullet import Bullet

def check_event(setting,screen,ship,bullet):
	""" 响应按钮和鼠标的事件 """
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_event(event,screen,setting,ship,bullet)
		elif event.type == pygame.KEYUP:
			check_keyup_event(event,setting,ship)

def check_keydown_event(event,screen,setting,ship,bullet):
 	if event.key == pygame.K_RIGHT:
 		ship.moving_right = True
 	elif event.key == pygame.K_LEFT:
 		ship.moving_left = True
 	elif event.key == pygame.K_SPACE:
 		new_bullet = Bullet(setting,screen,ship)
 		bullet.add(new_bullet)

def check_keyup_event(event,setting,ship):
 	if event.key == pygame.K_RIGHT:
 		ship.moving_right = False
 	elif event.key == pygame.K_LEFT:
 		ship.moving_left = False


def update_screen(screen_setting,screen,ship,bullet):
	""" 更新屏幕图像 切换到新的屏幕 """
	# 每次循环时重新绘制
	screen.fill(screen_setting.bg_color)
	for bull in bullet.sprites(): 
		bull.drew_bullet()
	ship.blitme()
	pygame.display.flip()
