#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/11/6 20:53
# @Author : Yang Peihao
# @Site : 
# @File : RandomizedWorst.py
# @Software: PyCharm
from pandas import np
import sys
sys.setrecursionlimit(100000)
from first.QickSortByFirst import partition_by_first
import time
def randomized_select(arr:"List[int]",p:"数组的左界",r:"数组的右界",k):
    if(p==r):
        return arr[p]
    i=partition_by_first(arr,p,r)
    j=i-p+1
    if(k<=j):
        return randomized_select(arr,p,i,k)
    else:
        return randomized_select(arr,i+1,r,k-j)
np.random.seed(123)
arr = np.random.randint(1000000000, size=int(20000))
arr = arr.tolist()
arr=sorted(arr)
k=2000
len=len(arr)
now_time = time.time()  ##2##
test=randomized_select(arr,0,len-1,k)
total_time = time.time() - now_time  ##3##
print("在利用partion函数线性选择基础上，最坏情况的分析：")
print("元素个数为",len)
print(f"最简单的查找第{ k }小的元素的结果为",test)
print(f"所花费的时间为",total_time)