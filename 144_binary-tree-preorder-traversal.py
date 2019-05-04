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

# ------------------中序遍历（迭代）--------------------
# 参考链接：https://github.com/allenwangyuan/coding_in_Python/blob/master/2_2_1_3_%E4%BA%8C%E5%8F%89%E6%A0%91%E4%B8%AD%E5%BA%8F%E9%81%8D%E5%8E%86.py
def inOrder2(pRoot):
    node = pRoot.left
    stack = [pRoot]
    while node:
        stack.append(node)
        node = node.left
    while stack:
        node = stack.pop()
        print node.val
        if node.right:
            node = node.right
            while node:
                stack.append(node)
                node = node.left

def inOrder2_1(pRoot):
    node = pRoot
    stack = []
    while True:
        while node:
            stack.append(node)
            node = node.left
        if stack:
            node = stack.pop()
            print node.val
            node = node.right
        else:
            break
