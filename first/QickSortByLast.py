#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/11/4 8:18
# @Author : Yang Peihao
# @Site : 
# @File : QickSortByLast.py
# @Software: PyCharm
import time  ##1##
import datetime
import numpy as np
def partition_by_last(arr:"待排序数组", low, high):
    # 此函数通过双指针的方式将数组进行排序，以最后一个元素为基准进行排序
    i = (low - 1)  # 最小元素索引
    pivot = arr[high]
    for j in range(low, high):
        # 当前元素小于或等于 pivot
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)


# arr[] --> 排序数组
# low  --> 起始索引
# high  --> 结束索引

# 快速排序函数
#值得注意的是快速排序的思路，我们找一个基准，将小于基准的元素放在左边，将大于基准的元素放在右面（通过交换两个元素来实现）
def quick_sort(arr, low, high):
    # 如果左面的指针小于右面的指针，即二者没有相遇
    if low < high:
        pi = partition_by_last(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)




# dt=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
# ts = int(time.mktime(time.strptime(dt, "%Y-%m-%d %H:%M:%S")))
# print("得到的ts为",ts)
# np.random.seed(123)
# arr=np.random.randint(ts,size=int(ts/1000))
# arr=arr.tolist()
arr=[1,6,9,8,45,55,66,100,1025,1024,2,3,6,5,4,8,5,45]
n = len(arr)
now_time = time.time()  ##2##
quick_sort(arr, 0, n - 1)
total_time = time.time() - now_time  ##3##
res=[]
print("排序后的数组:")
for i in range(n):
    res.append(arr[i])
print(res)
print(f"对于含有{n}个元素，基准元素为最后一个元素的快速排序算法消耗的时间为{total_time}")
