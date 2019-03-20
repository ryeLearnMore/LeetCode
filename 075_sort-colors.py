#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@author: rye
#@time: 2019/3/20

'''
此题有很多种方法：https://github.com/ryeLearnMore/awesome-algorithm/blob/master/docs/Leetcode_Solutions/Python/075._sort_colors.md

'''
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        flag0 = flag1 = flag2 = 0
        for i in nums:
            if i == 0:
                flag0 += 1
            elif i == 1:
                flag1 += 1
            else:
                flag2 += 1

        for i in range(len(nums)):
            if flag0 != 0:
                nums[i] = 0
                flag0 -= 1
            elif flag1 != 0:
                nums[i] = 1
                flag1 -= 1
            else:
                nums[i] = 2
                flag2 -= 1

        return nums

class Solution1(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        l, r = 0, len(nums) - 1
        i = 0
        while i <= r:
            if nums[i] == 0:
                nums[i], nums[l] = nums[l], nums[i]
                l += 1
                i += 1
            elif nums[i] == 1:
                i += 1
            else:
                nums[i], nums[r] = nums[r], nums[i] #　此处不能直接让i += 1，因为交换后的值还不值到是多少，不能草率决定
                r -= 1
        # begin, cur, end = 0, 0, len(nums) - 1
        #
        # while cur <= end:
        #     if nums[cur] == 0:
        #         nums[begin], nums[cur] = nums[cur], nums[begin]
        #         cur += 1
        #         begin += 1
        #     elif nums[cur] == 1:
        #         cur += 1
        #     else:  # nums[cur] == 2
        #         nums[cur], nums[end] = nums[end], nums[cur]
        #         end -= 1

        return nums

if __name__ == '__main__':
    nums = [2,0,2,0,1,0]
    nums1 = [1,2,0]
    print(Solution1().sortColors(nums))