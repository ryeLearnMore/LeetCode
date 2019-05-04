#!/usr/bin/env python
#coding:utf-8
#@author: rye
#@time: 2019/5/4 10:59

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 迭代
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        if not root:
            return None
        res = []
        stack = []
        stack.append(root)
        while len(stack) != 0:
            tmp = stack.pop()
            res.append(tmp.val)
            if tmp.right:
                stack.append(tmp.right)
            if tmp.left:
                stack.append(tmp.left)
        return res

# 递归1
class Solution1(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if not root:
            return res
        res.append(root.val)
        # python中append和extend的区别：
        # https://www.cnblogs.com/subic/p/6553187.html
        if root.left:
            res.extend(self.preorderTraversal(root.left))
        if root.right:
            res.extend(self.preorderTraversal(root.right))
        return res

# 递归2
class Solution2(object):
    def front(self,root,a):
        if root:
            a.append(root.val)
            self.front(root.left,a)
            self.front(root.right,a)
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        a = []
        if root == None:
            return a
        self.front(root,a)
        return a