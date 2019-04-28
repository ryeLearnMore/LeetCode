#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@author: rye
#@time: 2019/3/20

# 这是什么神仙思路啊，好难。。。
'''
想到有可能用递归去做，但是真的不知道怎么实现。多学习。。。

其他解题思路：https://github.com/ryeLearnMore/awesome-algorithm/blob/master/docs/Leetcode_Solutions/Python/078._Subsets.md

19.3.23。又看了一遍，觉得这种回溯方法设计的很巧妙，值得多学习，多看几遍。
'''

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []

        def search(tmp_res, idx):
            if idx == len(nums):
                res.append(tmp_res)
            else:
                search(tmp_res + [nums[idx]], idx + 1)
                search(tmp_res, idx + 1)

        search([], 0)
        return res

# --------------------19.4.28----------又有点忘了------------
# 结果：[[1, 2, 3], [1, 2], [1, 3], [1], [2, 3], [2], [3], []]
'''
根据递归的思想:因为解题方式不变，所以把大规模的问题分解为小规模的问题，
            可以观察到[[1, 2, 3], [1, 2], [1, 3], [1] ||| [2, 3], [2] ||| [3] ||| []]
            先1不动，让2，3去变化，然后2不动，让3去变化，以此类推。。。
            基于上述思想，可以总结为解题方式为：先让第一个元素不动，找出后面的子集，然后让第二个元素不动
            找出后面的子集。。。
            
            idx是关键！
'''
def subsets(nums):
    res = []
    def search(tmp_res, idx):
        if len(nums) == idx:
            res.append(tmp_res)
        else:
            search(tmp_res + [nums[idx]],idx + 1)
            search(tmp_res, idx + 1)

    search([], 0)
    return res

if __name__ == '__main__':
    nums = [1, 2, 3]
    print(Solution().subsets(nums))
    print(subsets(nums))