#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@author: rye
#@time: 2019/3/17

'''
未解出。
此题本想用递归的方法做出，但是由于只是的欠缺，没有找到为了一层结束之后不继续执行i + 1的操作。
tips：不一定非要找到恰好找到最后一个值的所有方法，只要reach大于len(nums)即可。无形之中给自己填了很多难度。这样
很不好。
'''
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # if nums[0] == 0 and len(nums) == 1:
        #     return True
        # elif nums[0] == 0 and len(nums) != 1:
        #     return False

        def check(nums, length):
            if nums[0] == 0 and length == 1:
                return True
            elif nums[0] == 0 and length != 1:
                return False

            for i in range(nums[0]):
                # if nums == []:
                #     return False
                if i + 1 == len(nums) - 1:
                    return True
                if i + 1 < len(nums) - 1:
                    if nums[i + 1] == 0:
                        return
                    else:
                        return check(nums[i + 1:], length)
                else:
                    return False

        length = len(nums)
        return check(nums, length)

'''
大佬的代码，采用了动态规划的思想。只用一个变量记录可达最远距离。
'''
class Solution1(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return True
        if len(nums) == 1:
            return True
        idx, reach = 0, 0
        n = len(nums)

        while idx <= reach and idx < n:
            reach = max(reach, nums[idx] + idx)
            idx += 1
        return reach >= n - 1


if __name__ == '__main__':
    nums = [2,3,1,1,4]
    nums1 = [3,2,1,0,4]
    nums2 = [2, 3]
    print(Solution1().canJump(nums2))