#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/11/6 13:43
# @Author : Yang Peihao
# @Site :
# @File : RandomizedSelect.py
# @Software: PyCharm
#该算法通过Randompartion函数在平均时间复杂度为O(n),并且最坏情况下其时间复杂度为O(n^2)，因为有可能我们每次产生的
#基准元素都是最大的或者是最小的元素
from pandas import np
from first.QickSortByRandom import partition_by_random
import time
def randomized_select(arr:"List[int]",p:"数组的左界",r:"数组的右界",k):
    if(p==r):
        return arr[p]
    i=partition_by_random(arr,p,r)
    j=i-p+1
    if(k<=j):
        return randomized_select(arr,p,i,k)
    else:
        return randomized_select(arr,i+1,r,k-j)
np.random.seed(123)
arr = np.random.randint(10000, size=int(2000000))
arr = arr.tolist()
k=500000
len=len(arr)
now_time = time.time()  ##2##
test=randomized_select(arr,0,len-1,k)
total_time = time.time() - now_time  ##3##
print("以随机数为基准的，利用Partiton函数的选择方法")
print("总数据量为",len)
print(f"最简单的查找第{ k }小的元素的结果为",test)
print(f"所花费的时间为",total_time)
