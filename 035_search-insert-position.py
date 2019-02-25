#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@author: rye
#@time: 2019/2/25

'''
当然可以用二分法加快查找速度。
'''
class Solution:
    def searchInsert(self, nums: 'List[int]', target: 'int') -> 'int':
        if target in nums:
            return nums.index(target)
        else:
            if target > nums[-1]:
                return len(nums)
            elif target < nums[0]:
                return 0
            else:
                for i in range(len(nums)):
                    if target < nums[i]:
                        return i

# 大佬的代码
# 找到第一个比target大的值的index，如果没找到则返回len(nums),但是代码中直接返回i值就行了
class Solution1(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        i = 0
        while nums[i] < target:
            i += 1
            if i == len(nums):
                return i
        return i

# 二分法
class Solution2(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + ((r-l) >> 1)
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return l


if __name__ == '__main__':
    nums = [1, 3, 5, 6]
    target = 7
    print(Solution().searchInsert(nums, target))