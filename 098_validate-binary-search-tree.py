#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@author: rye
#@time: 2019/3/29

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

'''
解题思路：
利用二叉树中序遍历的特点，如果中序遍历为升序，则说明该二叉树为有效搜索二叉树
'''

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        minN = float('-inf')
        # res = []
        if not root:
            return True

        stack = []
        node = root
        while node or (len(stack) > 0):
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                # res.append(node.val)
                if minN < node.val:
                    minN = node.val
                else:
                    return False
                node = node.right

        return True

if __name__ == '__main__':
    pass 