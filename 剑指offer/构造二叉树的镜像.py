#!/usr/bin/env python
#coding:utf-8
#@author: rye
#@time: 2019/6/23 16:08

# -*- coding:utf-8 -*-
'''
学习如何构造镜像二叉树，方法真的很简单。。。但是要知道才觉得简单！
PS：与leetcode上的判断“是否为镜像二叉树”做对比
'''


# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here
        if root != None:
            root.left, root.right = root.right, root.left
            self.Mirror(root.left)
            self.Mirror(root.right)
        return root