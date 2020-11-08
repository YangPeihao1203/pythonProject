#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/11/4 9:10
# @Author : Yang Peihao
# @Site :
# @File : BinarySearch.py
# @Software: PyCharm

import time  ##1##
import datetime
import numpy as np
# 返回 x 在 arr 中的索引，如果不存在返回 -1
def binary_search(arr, l, r, x):
    if r >= l:
        mid = int(l + (r - l) / 2)
        # 元素在中间位置
        if arr[mid] == x:
            return mid
            # 元素小于中间位置的元素，只需要再比较左边的元素
        elif arr[mid] > x:
            return binary_search(arr, l, mid - 1, x)
            # 元素大于中间位置的元素，只需要再比较右边的元素
        else:
            return binary_search(arr, mid + 1, r, x)
    else:
        # 不存在
        return -1

# dt=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
# ts = int(time.mktime(time.strptime(dt, "%Y-%m-%d %H:%M:%S")))
# x =1603031137
# np.random.seed(123)
# arr=np.random.randint(ts,size=int(ts/100))
# arr=arr.tolist()
arr=[2,3,6,4,1,0,0,16,5,2,2]
x=5
print("排序之前的数组为",arr)
arr=sorted(arr)
print("排序之后得到的数组为",arr)
now_time = time.time()  ##2##
print("排序的个数为",len(arr))
result = binary_search(arr, 0, len(arr) - 1, x)
if result != -1:
    print(f"查找的元素为{x},元素在数组中的索引为 %d" % result)
else:
    print("元素不在数组中")
total_time = time.time() - now_time  ##3##
print("该算法消耗的时间为",total_time)
