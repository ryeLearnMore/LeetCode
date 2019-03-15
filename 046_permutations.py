#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@author: rye
#@time: 2019/3/15

'''
这种递归题，对于现在的我来说，还是比较难啊。
觉得能独自写出这种代码的人还是很厉害的。最起码我现在写不出来。
'''
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [nums]
        res = []
        for i in range(len(nums)):
            prefix = nums[i]
            rest = nums[:i] + nums[i+1:]
            for j in self.permute(rest):
                res.append([prefix]+j)
        return res

class Solution1(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [nums]
        res = []
        for i in range(len(nums)):
            perfix = nums[i]
            rest = nums[:i] + nums[i + 1:]
            for j in self.permute(rest):
                res.append([perfix] + j)
        return res

if __name__ == '__main__':
    nums = [1,2,3,4]
    print(Solution().permute(nums))