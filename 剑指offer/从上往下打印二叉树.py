#!/usr/bin/env python
#coding:utf-8
#@author: rye
#@time: 2019/6/23 21:34

# -*- coding:utf-8 -*-
'''
这题考察层次遍历，与leetcode中的102题相似，但是更简单点。
tips：
    这题坑有点多，要多注意！
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        res = []
        if not root:
            return []  # 此处None
        queue = [root]
        while len(queue) != 0:
            r = queue.pop(0)
            res.append(r.val)
            if r.left:
                queue.append(r.left)
            if r.right:
                queue.append(r.right)
        return res