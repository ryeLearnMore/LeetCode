#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@author: rye
#@time: 2019/3/22

'''
此题是33题的变式，所以应该有一个基本思想，即：尽量找出两个题的差别，然后凑出上一题的形式
新加的代码就是为了凑出之前的形式！

参考链接：
https://github.com/apachecn/awesome-algorithm/blob/master/docs/Leetcode_Solutions/Python/0081._Search_in_Rotated_Sorted_Array_II.md
'''
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        l, r = 0, len(nums) - 1
        while l <= r:

            while l < r and nums[l] == nums[r]:  # 加上这两行就跟第33题一样了，个人觉得增加这行代码的意义是凑出33题的那种格式
                l += 1

            mid = l + ((r - l) >> 1)
            if nums[mid] == target:
                return True
            if nums[mid] <= nums[r]: # 这里还加了一个等号
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1

        return False

if __name__ == '__main__':
    nums = [2, 5, 6, 0, 0, 1, 2]
    nums1 = [1,1,3,1] #这个题就是针对增加的那两行
    target = 3
    print(Solution().search(nums1, target))