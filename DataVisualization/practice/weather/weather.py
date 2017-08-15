import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename = "sitka.csv"

# 获取最高温度
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)
	for index,column_header in enumerate(header_row):
		print(index,column_header)

	dates,highs,lows = [],[],[]
	for row in reader:
		try:
			current_date = datetime.strptime(row[0],"%Y-%m-%d")	
			low = int(row[5])
			high = int(row[1])
		except:
			print(current_date,',missing data')	
		else:
			dates.append(current_date)
			lows.append(low)
			highs.append(high)
	print(highs)

# 根据数据绘制图形
fig = plt.figure(dpi=128,figsize=(8,6))
plt.plot(dates,highs,c='red',alpha=0.8)
plt.plot(dates,lows,c='Blue',alpha=0.8)
plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)
# 设置图形的格式
plt.title("Daliy high temperature ",fontsize=24)
plt.xlabel('',fontsize=10)
plt.ylabel('temperature (F)',fontsize=16)
fig.autofmt_xdate()
plt.tick_params(axis='both',which='major',labelsize=16)
plt.show()















