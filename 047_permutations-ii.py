#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@author: rye
#@time: 2019/3/15

'''
跟第46题一样，就是最后append的时候不一样，只有没有结果里面没有的才加入
'''

class Solution(object):
    def permuteUnique(self, nums):
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
            for j in self.permuteUnique(rest):
                if [prefix] + j not in res:
                    res.append([prefix]+j)
        return res

if __name__ == '__main__':
    nums = [1, 1, 2]
    print(Solution().permuteUnique(nums))