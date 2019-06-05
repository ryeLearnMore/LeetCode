#!/usr/bin/env python
#coding:utf-8
#@author: rye
#@time: 2019/6/5 23:43

# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if len(pre) == 0: # 此处牛客网不能用if pre == None:
            return None
        root = TreeNode(pre[0])
        k = tin.index(pre[0])
        root.left = self.reConstructBinaryTree(pre[1:k + 1], tin[:k])
        root.right = self.reConstructBinaryTree(pre[k + 1:], tin[k + 1:])
        return root
