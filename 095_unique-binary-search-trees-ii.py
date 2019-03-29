#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@author: rye
#@time: 2019/3/29

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
'''
参考链接：
https://github.com/apachecn/awesome-algorithm/blob/master/docs/Leetcode_Solutions/Python/0095._Unique_Binary_Search_Trees_II.md

知道是用递归，但是还不知道怎么写。看了答案感觉不是完全懂，有空还得再看看。
'''

class Solution:
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []

        def helper(nums):
            if not nums:
                return [None]
            res = []
            for idx, num in enumerate(nums):
                for l in helper(nums[:idx]):
                    for r in helper(nums[idx + 1:]):
                        node = TreeNode(num)
                        node.left = l
                        node.right = r
                        res.append(node)
            return res

        return helper(list(range(1, n + 1)))

if __name__ == '__main__':
    n = 3
    print(Solution().generateTrees(n))