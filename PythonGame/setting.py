
class Settings(object):
	""" 存储所有的设置"""
	def __init__(self):
		''' 初始化设置 '''
		# 屏幕设置
		self.screen_width = 1000
		self.screen_height = 600
		self.bg_color = (230,230,230)

		# 飞船参数
		self.ship_speed_facter = 2;
		
		#子弹参数
		self.bullet_speed_facter = 1;
		self.bullet_width = 3
		self.bullet_height = 10
		self.bullet_color = (60,60,60)

		
		