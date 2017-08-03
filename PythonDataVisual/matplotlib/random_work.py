
import matplotlib.pyplot as plt
from random import choice

class  RandomWork():
	""" RandomWork """
	def __init__(self,num_points=500):
		self.num_points = num_points
		# 随机漫步
		self.x_values = [0]
		self.y_values = [0]

	def fill_walk(self):
		""" calculate point """
		while len(self.x_values)<self.num_points:
			x_direction = choice([1,-1])
			x_distance = choice([0,1,2,3,4])
			x_step = x_direction * x_distance

			y_direction = choice([-1,1])
			y_distance = choice([0,1,2,3,4])
			y_step = y_direction * y_distance

		 	#拒绝原地踏步
			if x_step == 0 and y_step == 0:
		 		continue

		 	#计算下一个点的x值和y值
			next_x = self.x_values[-1] + x_step
			next_y = self.y_values[-1] + y_step

			self.x_values.append(next_x)
			self.y_values.append(next_y)

while True:
	rw = RandomWork()
	rw.fill_walk()
	point_numbers = list(range(rw.num_points))
	plt.scatter(rw.x_values,rw.y_values,c=point_numbers,cmap=plt.cm.Blues,edgecolor='none',s=15)
	plt.show()

	keep_running = input("Make another walk?(y/n): ")
	if keep_running == 'n':
		break


