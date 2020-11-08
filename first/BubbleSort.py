#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/11/4 9:13
# @Author : Yang Peihao
# @Site : 
# @File : BubbleSort.py
# @Software: PyCharm





# 冒泡排序
import datetime
import time

from pandas import np


def bubbleSort(arr):
    n = len(arr)

    # 遍历所有数组元素
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]




# dt=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
# ts = int(time.mktime(time.strptime(dt, "%Y-%m-%d %H:%M:%S")))
# np.random.seed(123)
# arr=np.random.randint(ts,size=int(ts/100000))
# arr=arr.tolist()
arr=[1,6,9,8,45,55,66,100,1025,1024,2,3,6,5,4,8,5,45]
n = len(arr)
now_time = time.time()  ##2##
bubbleSort(arr)
total_time = time.time() - now_time  ##3##
res=[]
print("排序后的数组:")
for i in range(n):
    res.append(arr[i])
print(res)
print(f"对于含有{n}个元素，采用冒泡排序算法消耗的时间为{total_time}")