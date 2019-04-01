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
解法：
1. copy the left and right subtree
2. then cut root’s left subtree
3. do DFS
4. left and right has been flattened and connect them left and right back to the root
'''

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        left_node = root.left
        right_node = root.right
        root.left = None
        self.flatten(left_node)
        self.flatten(right_node)
        if left_node:
            root.right = left_node # 相对于链表插入的第一步
            while left_node.right:
                left_node = left_node.right
            left_node.right = right_node # 相对于链表插入的第二步

# 另一个大佬的代码
class Solution1(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:
            return root
        self.flatten(root.left)
        self.flatten(root.right)
        while root.left is not None:
            right = root.right
            root.right = root.left # 插入第一步
            root.left = None
            node = root.right # 插入第二步
            while node.right is not None:
                node = node.right
            node.right = right

if __name__ == '__main__':
    pass 