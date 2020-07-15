# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 14:17:22 2020

@author: zhy
"""


from numpy import *
import matplotlib.pyplot as plt
import pylab

def loadData(str):
    f = open(str)
    lines = f.readlines() 
    x=[]
    y=[]          #把全部数据文件读到一个列表lines中
    A_row = 0                       #表示矩阵的行，从0行开始
    for line in lines:              #把lines中的数据逐行读取出来
        list = line.strip('\n').split(' ')      #处理逐行数据：strip表示把头尾的'\n'去掉，split表示以空格来分割行数据，然后把处理后的行数据返回到list列表中
        x.append(double(list[0]))                    #把处理后的数据放到方阵A中。list[0:3]表示列表的0,1,2列数据放到矩阵A中的A_row行
        y.append(double(list[1])/1000) 
    return x,y;

    
    return x,y;
if __name__ == '__main__':
   #filename = "entityVector.txt"
   x,y=loadData("1.txt");
   fig = plt.figure()
   ax = fig.add_subplot(111)
   print(x);
   plt.plot(x[0:400],y[0:400]);
   plt.title('loss-time')
   plt.xlabel('time')
   plt.ylabel('loss*1000')
   print("ddd")
   plt.show()