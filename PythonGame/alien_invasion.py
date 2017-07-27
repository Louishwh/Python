
import sys
import pygame
from setting import Settings
from ship import Ship
from pygame.sprite import Group

import game_founctions as gf

def run_game():
	# 初始化 并创建屏幕 
	pygame.init()

	g_setting = Settings()

	screen = pygame.display.set_mode((g_setting.screen_width,g_setting.screen_height))
	pygame.display.set_caption("Alien Invasion")

	ship = Ship(g_setting,screen)

	bullets = Group()

	# 开始主循环
	while True:

		# 监控鼠标和键盘
		gf.check_event(g_setting,screen,ship,bullets)
		ship.update()
		bullets.update()
		gf.update_screen(g_setting, screen,ship,bullets)

run_game()


