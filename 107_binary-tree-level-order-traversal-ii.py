#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@author: rye
#@time: 2019/3/30

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        if not root:
            return res
        queue = []
        queue.append(root)
        while len(queue) != 0:
            tmp = []
            for i in range(len(queue)):
                p = queue.pop(0)
                if p.left:
                    queue.append(p.left)
                if p.right:
                    queue.append(p.right)
                tmp.append(p.val)
            res.append(tmp)
        return res[::-1]


if __name__ == '__main__':
    pass 