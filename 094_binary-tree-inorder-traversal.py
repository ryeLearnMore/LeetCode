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

# 递归
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        res = []
        def travel(root, res):
            if root == None:
                return
            travel(root.left, res)
            res.append(root.val)
            travel(root.right, res)
        travel(root, res)
        return res

# 非递归
'''
解题思路：
参考链接：https://github.com/ryeLearnMore/awesome-algorithm/blob/master/docs/Leetcode_Solutions/Python/094._binary_tree_inorder_traversal.md
先一股脑把左边一条线全部push到底（即走到最左边），然后node最终为None了就开始pop stack了，
然后因为pop出来的每一个node都是自己这棵树的root，所以看看它有没有右孩子，没有那肯定继续pop，
有的话自然而然右孩子是下一个要被访问的节点。
'''
class Solution1(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if not root:
            return res

        stack = []
        node = root
        while node or (len(stack) > 0):
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                res.append(node.val)
                node = node.right
        return res

if __name__ == '__main__':
    tree = [1, None, 2, 3]
    print(Solution().inorderTraversal(tree))