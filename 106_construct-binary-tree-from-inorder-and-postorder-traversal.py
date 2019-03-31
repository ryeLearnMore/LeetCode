#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@author: rye
#@time: 2019/3/31

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
'''
仿照上一题（105题）的思想做的
注意：
注意中序和后序两个列表的取值（方法：随便拿一个值去试就可以）。
'''
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not postorder and len(postorder) == 0:
            return None
        root = TreeNode(postorder[-1])
        k = inorder.index(postorder[-1])

        root.left = self.buildTree(inorder[:k], postorder[:k])
        root.right = self.buildTree(inorder[k + 1:], postorder[k:-1])

        return root

if __name__ == '__main__':
    pass 