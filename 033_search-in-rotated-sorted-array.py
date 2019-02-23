#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@author: rye
#@time: 2019/2/23
'''
个人觉得方法比较简单，就是二分法。
只不过len(nums) == 1 or 2 or 顺序排列的情况，需要仔细讨论，比较麻烦，调了12次才过。而且我写的冗余度太高

tips: 多看看下面大佬的算法，好好理解！
'''
class Solution:
    def search(self, nums: 'List[int]', target: 'int') -> 'int':

        if len(nums) == 0:
            return -1
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1

        for i in range(len(nums)):
            if i + 1 < len(nums):
                if nums[i + 1] < nums[i]:
                    point = i
                    break
            else: # 我觉得此时只可能len(nums) == 2
                # 说明此list应该是升序或降序
                # if nums[0] == target:
                #     return 0
                # elif nums[1] == target:
                #     return 1
                # else:
                #     return -1
                i = 0
                j = len(nums) - 1
                while i < j:
                    if (i + j) % 2 == 1:
                        point = (i + j + 1) // 2
                    else:
                        point = (i + j) // 2
                    if j == i + 1:
                        if nums[j] == target:
                            return j
                        elif nums[i] == target:
                            return i
                        break
                    elif nums[point] == target:
                        return point
                    elif target > point:
                        i = point
                    else:
                        j = point

        i = 0
        j = len(nums) - 1
        if target >= nums[i]:
            j = point
        elif target <= nums[j]:
            i = point + 1
        if i == j:
            if nums[i] == target:
                return i
            else:
                return -1

        while i < j:
            if (i + j) % 2 == 1:
                point = (i + j + 1) // 2
            else:
                point = (i + j) // 2
            if j == i + 1:
                if nums[j] == target:
                    return j
                elif nums[i] == target:
                    return i
                break
            elif nums[point] == target:
                return point
            elif target > nums[point]:
                i = point
            else:
                j = point

        return -1

# 大佬的代码
class Solution1(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + ((r - l) >> 2) # 此处应该是l + ((r - l ) >> 1)吧。。。
            if nums[mid] == target:
                return mid
            if nums[mid] < nums[r]: # 分了两种情况讨论
                if nums[mid] < target <= nums[r]: # 如果target处于两段有序中的一段呢。此处是右边的一段
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if nums[l] <= target < nums[mid]: # 此处是左边的一段
                    r = mid - 1
                else:
                    l = mid + 1
        return -1


if __name__ == '__main__':
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 0
    nums1 = [15,16,19,20,25,1,3,4,5,7,10,14]
    target1 = 26
    nums2 = [3, 5, 1]
    target2 = 1
    nums3 = [3, 1]
    target3 = 0
    nums4 = [4,5,6,7,0,1,2]
    target4 = 2
    print(Solution1().search(nums4, target4))