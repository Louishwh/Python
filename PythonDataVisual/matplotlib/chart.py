import matplotlib.pyplot as plt


''' 折线统计图 '''

# 获取数据
# # input_value = [1,2,3,4,8,9,8,85,10,9,8,7,6,11]
# input_value = [1,2,3,4,5,6,7,8,9,10]
# squares = [x*x for x in input_value]
# # 导入数据
# plt.plot(input_value,squares,linewidth=3)
# 
# 设置表的样式
# plt.title("Random Number",fontsize=18)
# plt.xlabel("xlabel",fontsize=12)
# plt.ylabel("ylabel",fontsize=12)
# plt.tick_params(axis='both',labelsize=14)
# plt.axis = ([0,1100,0,11000000])
# # 显示数据
# plt.show()

''' 散点统计图 '''

x_values = list(range(1,999))
y_values = [x**2 for x in x_values]
plt.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Reds,edgecolor='none',s=10)
plt.show()
plt.savefig('squares_plot.png',bbox_inches='tight')











