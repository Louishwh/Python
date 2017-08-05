#! /usr/bin/env python   
# -*- coding: utf-8 -*-   
import requests
import json
import os
from github_analyze import graphing

#调用的api
target_place = "https://api.github.com/search/repositories?q=language:"
languages = ['Python','Java','Ruby','Go','Perl','Swift','Objective-C']
# languages = ['Objective-C']
# languages = ['Java']
sorted_type = "&sort=stars"

# 获取所有返回的结果
response_dicts = []
name,starcount,urls = [],[],[]

for index,language in enumerate(languages):
	name,starcount,urls = [],[],[]
	response = requests.get(target_place+language+sorted_type)
	response_dicts.append(response.json())
	try:
		count = float(response_dicts[index]['total_count'])/10000
		items= response_dicts[index]['items']
		print(language+" count in github: "+str(count)+"w")
		
		for item in items:
			name.append(item['name'])
			starcount.append(item['stargazers_count'])
			urls.append(item['clone_url'])

		graphing(languages[index],name,starcount)
		os.popen('open -a Chrome '+language+"_repos.svg")
	except:
		print(language+' has wrong')

