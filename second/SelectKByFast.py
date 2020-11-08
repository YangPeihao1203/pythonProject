#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/11/6 13:42
# @Author : Yang Peihao
# @Site :
# @File : SelectKByFast.py
# @Software: PyCharm

#最简单的查找无序数组中第k小元素的方法------通过快排


import time  ##1##
from pandas import np

def fast_select(arr, k):
    arr=sorted(arr)
    return arr[k-1]


if __name__ == '__main__':
    np.random.seed(123)
    arr = np.random.randint(100, size=int(10000))
    arr = arr.tolist()
    k=144
    now_time = time.time()  ##2##
    test=fast_select(arr,k)
    total_time = time.time() - now_time  ##3##
    print(f"最简单的查找第{ k }小的元素的结果为",test)
    print(f"所花费的时间为",total_time)

