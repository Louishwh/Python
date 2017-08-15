##官网 http://www.pygal.org/ 
#
from random import randint
import pygal

class Die():
	def __init__(self, num_sides=6):
		self.num_sides = num_sides

	def roll(self):
		return randint(1,self.num_sides)

# 创建骰子 how about two die?
die1 = Die()

# 将结果存储到一个列表中
times = 10000
results = []
for roll_num in range(times):
	result = die.roll()
	results.append(result)
print(results)

# 分析结果
frequencies = []
for value in range(1,die.num_sides+1):
	frequency = results.count(value)
	frequencies.append(frequency)
print(frequencies)

#对结果可视化
hist = pygal.Bar()

hist.title = "Result of rolling one D6 %d times" % times
hist.x_labels = ['1','2','3','4','5','6']
hist.x_title = "Result"
hist.y_title = "Frequency of result"
hist.add('D6',frequencies)
hist.render_to_file('die_visualsvg')




