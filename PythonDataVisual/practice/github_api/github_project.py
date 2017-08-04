#! /usr/bin/env python   
# -*- coding: utf-8 -*-   
import requests
import json

#调用的api
target_place = "https://api.github.com/search/repositories?q=language:"
languages = ['Python','Java','Ruby','Go','Perl','Swift','Objective-C','C','C++','C#','PHP','Javascript']
sorted_type = "&sort=stars"

# 获取所有的URL
response_dicts = []
for index,language in enumerate(languages):
	target_url = target_place+language+sorted_type
	response = requests.get(target_url)
	response_dicts.append(response.json())
	print(response_dicts[index].keys())
	try:
		count = float(response_dicts[index]['total_count'])/10000
		print(language+" count in github: "+str(count)+"w")
	except:
		print(language+' has wrong')

