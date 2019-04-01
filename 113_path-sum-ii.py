#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@author: rye
#@time: 2019/4/1

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
'''
AC代码
仿照上一题的思想解决的，这一套路（res=[],path(root, sum, [])）之前的题也用到过，所以还是有用的。
多学习
'''
class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        res = []
        def path(root, sum, tmp):
            if not root:
                return
            elif root.left or root.right:
                return path(root.left, sum - root.val, tmp + [root.val]) or path(root.right, sum - root.val, tmp + [root.val])
            else:
                if root.val == sum:
                    tmp += [root.val]
                    res.append(tmp)
                    # return res # 这里不用return res
        path(root, sum, [])
        return res

# 用一种非递归的方式，借助队列，用前序遍历解决。
class Solution1(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """

        if not root:
            return []
        res = []
        queue = [(root, root.val, [root.val])]
        while queue:
            node, target, temp = queue.pop(0)
            if not node.left and not node.right and target == sum:
                res.append(temp)
            if node.left:
                queue.append((node.left, target+node.left.val, temp+[node.left.val]))
            if node.right:
                queue.append((node.right, target+node.right.val, temp+[node.right.val]))
        return res

if __name__ == '__main__':
    pass 