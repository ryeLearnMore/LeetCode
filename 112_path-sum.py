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
自己做没做出来，虽然知道用递归，但是没想到sum - root.val，一直考虑用cnt去等于sum，所以没有很好的解决。
'''
class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        elif root.left or root.right:
            return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)
        else:
            return root.val == sum


class Solution1(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """

        def has(root, sum):
            if not root.left and not root.right:
                return sum == root.val
            h = False
            if root.left:
                h = has(root.left, sum - root.val)
            if not h and root.right:
                h = has(root.right, sum - root.val)
            return h

        if not root:
            return False
        return has(root, sum)


if __name__ == '__main__':
    pass 