#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/11/6 13:42
# @Author : Yang Peihao
# @Site : 
# @File : SelectKByHeap.py
# @Software: PyCharm
#最简单的查找无序数组中第k小元素的方法------通过堆排序
import time  ##1##
from pandas import np

def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2
    if l < n and arr[i] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # 交换
        heapify(arr, n, largest)

def heapSort(arr):
    n = len(arr)
    # Build a maxheap.
    for i in range(n, -1, -1):
        heapify(arr, n, i)
        # 一个个交换元素
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # 交换
        heapify(arr, i, 0)
def heap_select(arr, k):
    heapSort(arr)
    return arr[k-1]
arr=[1,35,8,6,7,21]
k=2
np.random.seed(123)
arr = np.random.randint(10000, size=int(2000000))
arr = arr.tolist()
k=500000
now_time = time.time()  ##2##
test=heap_select(arr,k)
total_time = time.time() - now_time  ##3##
print(f"堆排序")
print("总数据量为",len(arr))
print(f"最简单的查找第{ k }小的元素的结果为",test)
print(f"所花费的时间为",total_time)


