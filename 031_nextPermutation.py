#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@author: rye
#@time: 2019/2/23

# 看这两个链接就能看懂这道题了
# https://www.jianshu.com/p/0fb544271bb5
# https://github.com/ryeLearnMore/awesome-algorithm/blob/master/docs/Leetcode_Solutions/Python/031._next_permutation.md
'''
全排序：
从n个不同元素中任取m（m≤n）个元素，按照一定的顺序排列起来，叫做从n个不同元素中取出m个元素的一个排列。当m=n时所有的排列情况叫全排列。例如n=3，全排序为：123、132、213、231、312、321共6种。

字典序法：
对给定的字符集中的字符规定了一个先后关系，在此基础上规定两个全排列的先后是：从左到右逐个比较对应的字符大小。字符集{1,2,3}，较小的数字较先，这样按字典序生成的全排列即：123、132、213、231、312、321。

1.现在假设输入全排序中的一串数字，要求得到它在字典序全排列中对应的下一个排列数。比如：输入123输出132，输入12435输出12453。

算法思想：

1.从数列的右边向左寻找连续递增序列, 例如对于：1,3,5,4,2，其中5-3-2即为递增序列。

2.从上述序列中找一个比它前面的数（3）大的最小数（4），并将且交换这两个数。于是1,3,5,4,2->1,4,5,3,2，此时交换后的依然是递增序列。

3.新的递增序列逆序，即：1,4,5,3,2 => 1,4,2,3,5
'''
# 用上述学到的思想，自己重写了一下，貌似时间复杂度编程O（n^2）了
class Solution:
    def nextPermutation(self, nums: 'List[int]') -> 'None':
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return

        for i in range(len(nums) - 1, -1, -1):
            if nums[i - 1] < nums[i]:
                if i != 0:
                    temp = nums[i - 1]
                    for j in range(len(nums) - 1, i - 1, -1):
                        if nums[j] > temp:
                            nums[i - 1] = nums[j]
                            nums[j] = temp
                            break
                    break
        nums[i:] = nums[i:][::-1]
        return nums

# 大佬的方法
class Solution1(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return
        idx = 0
        for i in range(len(nums)-1, 0, -1):
            if nums[i] > nums[i-1]: # find first number which is smaller than it's after number
                idx = i
                break
        if idx != 0: # if the number exist,which means that the nums not like{5,4,3,2,1}
            for i in range(len(nums)-1, idx-1, -1):
                if nums[i] > nums[idx-1]:
                    nums[i], nums[idx-1] = nums[idx-1], nums[i]
                    break

        nums[idx:] = nums[idx:][::-1]
        return nums

if __name__ == '__main__':
    nums = [1, 2, 4, 6, 5, 3]
    nums1 = [3,2,1]
    print(Solution().nextPermutation(nums1))