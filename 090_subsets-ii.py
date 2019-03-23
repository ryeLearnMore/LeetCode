#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@author: rye
#@time: 2019/3/23

'''
解题思路（5种）：
https://github.com/ryeLearnMore/awesome-algorithm/blob/master/docs/Leetcode_Solutions/Python/090._subsets_ii.md

不过前提是要理解78题。。。
'''

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        res = []
        def search(tmp_res, idx):
            if idx == len(nums):
                if sorted(tmp_res) not in res:
                    res.append(sorted(tmp_res))
            else:
                search(tmp_res + [nums[idx]], idx + 1)
                search(tmp_res, idx + 1)

        search([], 0)
        return res

if __name__ == '__main__':
    nums = [4,4,4,1,4]
    print(Solution().subsetsWithDup(nums))