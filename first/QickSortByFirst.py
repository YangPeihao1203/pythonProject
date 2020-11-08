#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/11/4 8:56
# @Author : Yang Peihao
# @Site : 
# @File : QickSortByFirst.py
# @Software: PyCharm
import time  ##1##
import datetime
import numpy as np
def partition_by_first(array:"待排序数组", low, high):
    # 此函数通过双指针的方式将数组进行排序，以第一个一个元素为基准进行排序
    key = array[low]
    while low < high:
        while low < high and array[high] >= key:
            high -= 1
        if low < high:
            array[low] = array[high]

        while low < high and array[low] < key:
            low += 1
        if low < high:
            array[high] = array[low]

    array[low] = key
    return low




# 快速排序函数
#值得注意的是快速排序的思路，我们找一个基准，将小于基准的元素放在左边，将大于基准的元素放在右面（通过交换两个元素来实现）
def quick_sort(arr, low, high):
    # 如果左面的指针小于右面的指针，即二者没有相遇
    if low < high:
        pi = partition_by_first(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

if __name__ == '__main__':
    dt=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    ts = int(time.mktime(time.strptime(dt, "%Y-%m-%d %H:%M:%S")))
    np.random.seed(123)
    arr=np.random.randint(ts,size=int(ts/1000))
    arr=arr.tolist()
    arr=[66, 92, 98, 17, 83, 57, 86, 97, 96, 47, 73, 32, 46, 96, 25, 83, 78, 36, 96, 80, 68, 49, 55, 67, 2, 84, 39, 66, 84, 47]
    n = len(arr)
    now_time = time.time()  ##2##
    quick_sort(arr, 0, n - 1)
    total_time = time.time() - now_time  ##3##
    res=[]
    print("排序后的数组:")
    for i in range(n):
        res.append(arr[i])
    print(res)
    print(f"对于含有{n}个元素，基准元素为第一个元素的快速排序算法消耗的时间为{total_time}")