#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@author: rye
#@time: 2019/4/8

# 冒泡排序
def bubble_sort(nums):
    '''关键点：记住两个循环中的range值'''
    n = len(nums)
    for i in range(n - 1): # 总共循环n-1次
        for j in range(n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums
'''bubble_sort()有两种优化，记录如下'''
# 参考链接：https://github.com/wuchong/Algorithm-Interview/blob/master/Sort/python/BubbleSort.py
#优化1：某一趟遍历如果没有数据交换，则说明已经排好序了，因此不用再进行迭代了。
#用一个标记记录这个状态即可。
def bubble_sort2(ary):
    n = len(ary)
    for i in range(n):
        flag = 1                    #标记
        for j in range(1, n-i):
            if ary[j-1] > ary[j]:
                ary[j-1], ary[j] = ary[j], ary[j-1]
                flag = 0
        if flag:                   #全排好序了，直接跳出
            break
    return ary

#优化2：记录某次遍历时最后发生数据交换的位置，这个位置之后的数据显然已经有序了。
# 因此通过记录最后发生数据交换的位置就可以确定下次循环的范围了。
def bubble_sort3(ary):
    n = len(ary)
    k = n                           #k为循环的范围，初始值n
    for i in range(n):
        flag = 1
        for j in range(1,k):        #只遍历到最后交换的位置即可
            if ary[j-1] > ary[j]:
                ary[j-1], ary[j] = ary[j], ary[j-1]
                k = j               #记录最后交换的位置
                flag = 0
        if flag :
            break
    return ary

# 选择排序
def selction_sort(nums):

    n = len(nums)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if nums[j] < nums[min_index]:
                min_index = j
        nums[i], nums[min_index] = nums[min_index], nums[i]

    return nums

# 插入排序
def insertionSort(alist):
    for i, item_i in enumerate(alist):
        print(alist)
        index = i
        while index > 0 and alist[index - 1] > item_i:
            alist[index] = alist[index - 1]
            index -= 1

        alist[index] = item_i

    return alist

# 不用枚举来做
def insert_sort1(ary):
    n = len(ary)
    for i in range(1,n):
        if ary[i] < ary[i-1]:
            temp = ary[i]
            index = i           #待插入的下标
            for j in range(i-1,-1,-1):  #从i-1 循环到 0 (包括0)
                if ary[j] > temp :
                    ary[j+1] = ary[j]
                    index = j   #记录待插入下标
                else :
                    break
            ary[index] = temp
    return ary

def insert_sort(nums):

    # for index, i in enumerate(1, nums): # TypeError: 'list' object cannot be interpreted as an integer
    for index, i in enumerate(nums):
        tmp_index = index
        while tmp_index > 0 and nums[tmp_index - 1] > i:
            nums[tmp_index] = nums[tmp_index - 1]
            tmp_index -= 1
        nums[tmp_index] = i
    return nums

# def shell_sort(nums):
#
#     n = len(nums)
#
#     gap = n // 2
#     # gap变化到0之前，执行插入算法的次数
#     while gap > 0:
#         # 插入算法，与普通的插入算法的区别就是缩小的是gap而不是1
#         for i in range(gap, n):
#             j = i
#             while j > 0:
#                 if nums[j] < nums[j - gap]:
#                     nums[j], nums[j - gap] = nums[j - gap], nums[j]
#                     j -= gap
#                 else:
#                     break
#         # 缩短gap步长
#         gap //= 2
#
#     return nums

def shell_sort1(ary):
    n = len(ary)
    # gap = round(n/2)       #初始步长 , 用round四舍五入取整
    gap = n // 2
    while gap > 0:
        for i in range(gap,n):        #每一列进行插入排序 , 从gap 到 n-1
            temp = ary[i]
            j = i
            while ( j >= gap and ary[j-gap] > temp ):    #插入排序
                ary[j] = ary[j-gap]
                j = j - gap
            ary[j] = temp
        # gap = round(gap/2)                     #重新设置步长
        gap //= 2
    return ary

# ----------------------------------------归并排序---------------------------
def merge_sort(ary):
    if len(ary) <= 1 : return ary
    num = int(len(ary)/2)       #二分分解
    left = merge_sort(ary[:num])
    right = merge_sort(ary[num:])
    return merge(left,right)    #合并数组

def merge(left,right):
    '''合并操作，
    将两个有序数组left[]和right[]合并成一个大的有序数组'''
    l,r = 0,0           #left与right数组的下标指针
    result = []
    while l<len(left) and r<len(right) :
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    result += left[l:] # 因为上一个while是and关系，存在一个有1个元素，另一个有两个最后漏掉一个的情况，所以需要用下面两行将剩下的加进result里
    result += right[r:]
    return result

# -------------------------快速排序---------------------
def quick_sort(nums):
    return qsort(nums, 0, len(nums) - 1)

def qsort(ary, left, right):

    if left >= right: return ary
    key = ary[left]
    lp = left
    rp = right
    while lp < rp:
        while ary[rp] >= key and lp < rp:
            rp -= 1
        while ary[lp] <= key and lp < rp:
            lp += 1
        ary[lp], ary[rp] = ary[rp], ary[lp]

    ary[left], ary[lp] = ary[lp], ary[left]
    qsort(ary, left, lp - 1)
    qsort(ary, rp + 1, right)
    return ary







if __name__ == '__main__':
    nums = [12,12,345,457,45,2,34,7,678,234,13]
    print(bubble_sort3(nums))
    # print(selction_sort(nums))
    # print(insertionSort(nums))
    # print(insert_sort(nums))
    # print(shell_sort(nums))
    # print(merge_sort(nums))
    # print(quick_sort(nums))