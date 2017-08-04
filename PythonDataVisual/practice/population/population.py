#! /usr/bin/env python   
# -*- coding: utf-8 -*-   
import json
import csv  
import pygal
from country_code import get_country_code
from pygal.style import RotateStyle

''' JSON '''
# # 将数据加载到一个列表中  
filename = 'population.json'
pop_data = []

with open(filename,encoding='utf-8') as f:
	try: 
		pop_data = json.load(f)
	except:
		print("...")
	else:
		pass

# 遍历json取出需要的数据
year = 2013
cc_populations = {}
for index,pop_dict in enumerate(pop_data):

	if pop_dict['Year'] == str(year):
		country_name = pop_dict['Country Name']
		population = int(float(pop_dict['Value']))/10000
		code = get_country_code(country_name)
		if code:
			cc_populations[code] = population
	# if index>8000:
	# 	if pop_dict['Year'] == str(year):
	# 		country_name = pop_dict['Country Name']
	# 		population = int(float(pop_dict['Value']))
	# 		code = get_country_code(country_name)
	# 		if code:
	# 			cc_populations[code] = population
	# else:
	# 	if pop_dict['Year'] == str(year):
	# 		country_name = pop_dict['Country Name']
	# 		population = int(float(pop_dict['Value']))
	# 		code = get_country_code(country_name)
	# 		if code:
	# 			cc_populations[code] = population

# 打印总的数据条数
print(len(cc_populations))
cc_pop_1,cc_pop_2,cc_pop_3 = {},{},{}
for cc,pop in cc_populations.items():
	if pop < 10000:
		print(123)

wm_style = RotateStyle('#336699')
wm = pygal.maps.world.World(style=wm_style)
wm.title = 'World population map of %s' %str(year)
wm.add(str(year),cc_populations)
wm.render_to_file('worldmap.svg')


