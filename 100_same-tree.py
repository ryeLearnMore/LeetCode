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
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p and q and p.val == q.val:
            return self.judge(p.left, q.left) and self.judge(p.right, q.right)
        elif p == q == None:# p and q都为[]时，为True
            return True
        else:
            return False

    def judge(self, p, q):
        if p == None and q == None:
            return True
        elif p and q and p.val == q.val:
            return self.judge(p.left, q.left) and self.judge(p.right, q.right)
        else:
            return False

# 比较简洁的代码
class Solution1(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:
            return True

        self.result = True
        self.check(p, q)
        return self.result

    def check(self, p, q):
        # if :
        if (not p or not q) or (p.val != q.val):
            self.result = False
            return

        if p.left or q.left:
            self.check(p.left, q.left)
        if p.right or q.right:
            self.check(p.right, q.right)

        return
if __name__ == '__main__':
    pass 