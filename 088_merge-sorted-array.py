#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@author: rye
#@time: 2019/3/22

'''
还是得多写代码找感觉啊，思想比较简单，但是自己动手写还是花了点时间。
tips:
1. 学习list的pop()方法

'''
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # 作弊
        # nums1[m:] = nums2
        # nums1.sort()

        # pop()方法
        # http: // www.runoob.com / python / att - list - pop.html
        for i in range(len(nums1) - m):
            nums1.pop()

        i, j = 0, 0

        if n != 0 or len(nums2) != 0:
            while i < n and j < m:
                if nums2[i] <= nums1[j]:
                    nums1.insert(j, nums2[i])
                    i += 1
                    m += 1
                j += 1

            while i < n:
                j += 1
                nums1.insert(j, nums2[i])
                i += 1

            return nums1

class Solution1(object):
    def merge(self, nums1, m, nums2, n):
        for i in range(len(nums1) - m):
            nums1.pop()
        j = 0
        for i in nums2:
            while j < m:
                if i <= nums1[j]:
                    nums1.insert(j, i)
                    break
                j += 1
            if j == m:
                nums1.insert(m + j, i)
            m += 1
        return nums1

# 大佬的代码
# 倒着看真的更简单啊
# https://github.com/ryeLearnMore/awesome-algorithm/blob/master/docs/Leetcode_Solutions/Python/088._merge_sorted_array.md
class Solution2:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        while m > 0 and n > 0:
            if nums1[m-1] > nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
        if n > 0:
            nums1[:n] = nums2[:n]

if __name__ == '__main__':
    # nums1 = [1, 2, 3, 0, 0, 0]
    # m = 3
    # nums2 = [2, 5, 6]
    # n = 3
    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    nums3 = [4, 0, 0, 0, 0, 0]
    m3 = 1
    nums4 = [1, 2, 3, 5, 6]
    n4 = 5
    print(Solution().merge(nums3, m3, nums4, n4))