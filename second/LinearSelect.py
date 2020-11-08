#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/11/6 13:45
# @Author : Yang Peihao
# @Site : 
# @File : LinearSelect.py
# @Software: PyCharm
#本算法为线性时间选择来选择无序数组中第k小的元素，线性时间选择的好处是可在即使是在最坏的情况下，
#也可以达到O（n）
import time
import second.SelectKByFast as BS
from pandas import n

global count,len
times=1;
def partition(a, left, right, x):
    i = left
    j = right
    while i < j:
        while a[j] > x and i < j:
            j -= 1
        while a[i] < x and i < j:
            i += 1
        a[i], a[j] = a[j], a[i]
        if(a[i]==a[j]):
            j-=1
    return i
def liner_select(arr:"List[int]",p,r,k):
    # print(arr)
    mid=[]
    if(r-p<75):
        return BS.fast_select(arr[p:r+1],k)
    for i in range(0,int((r-p)/5)+1):
        if(p+5*i+4<=r):
            temp=sorted(arr[(p+5*i):(p+5*i+5)])
            temp1=temp[2]
            mid.append(temp1)
        else:
            temp=sorted(arr[p+5*i:r+1])
            if(r==p+5*i):
             temp1=arr[r]
            else:
             temp1 = temp[(r-(p+5*i)+1)//2-1]
            mid.append(temp1)
    x=liner_select(mid[:],0,len(mid)-1,int(len(mid)/2))
    i=partition(arr,p,r,x)
    num=i-p+1;
    if(k<=num):
        return liner_select(arr,p,i,k)
    else:
        return liner_select(arr,i+1,r,k-num)
np.random.seed(123)
arr=np.random.randint(10000,size=int(2000000))
arr=arr.tolist()
arr=sorted(arr)
x=len(arr)
print("生成了",x ,"个数")
k = input('输入想要第几小的数字')
now_time = time.time()  ##2##
res=liner_select(arr, 0,x- 1, int(k))
total_time = time.time() - now_time  ##3##
print("线性时间选择")
print("最后的结果为",res)
print("花费的时间为",total_time)










