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
个人感觉这道题虽然是easy，但是还需要多做几遍。
'''
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def TreeHeight(node):
            if not node:
                return 0
            return 1 + max(TreeHeight(node.left), TreeHeight(node.right))

        if not root:
            return True
        if abs(TreeHeight(root.left) - TreeHeight(root.right)) > 1:
            return False
        else:
            return self.isBalanced(root.left) and self.isBalanced(root.right) #注意这步是关键
            # 不能写成下面的这种形式，因为and有返回True或False的作用
            # return self.isBalanced(root.left)
            # return self.isBalanced(root.right)

if __name__ == '__main__':
    pass 