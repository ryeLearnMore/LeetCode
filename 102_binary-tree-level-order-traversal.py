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
'''
非递归
考研的时候复习数据结构对这个很有印象，不过现在确实忘了。参考链接：https://blog.csdn.net/yurenguowang/article/details/76906620
看了参考链接才想起来。
'''
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []

        if not root:
            return res
        queue = []
        queue.append(root)
        while len(queue) != 0:
            tmp = []
            for i in range(len(queue)):
                r = queue.pop(0)
                if r.left:
                    queue.append(r.left)
                if r.right:
                    queue.append(r.right)
                tmp.append(r.val)
            res.append(tmp)

        return res

# 也可以考虑递归（个人不太喜欢用递归）
'''
因为res的下标被控制了，所以只需要用dfs搜索到所有节点，控制到对应下标就行。
'''
class Solution1:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        def dfs(node, level, res):
            if not node:
                return
            if len(res) < level:
                res.append([])
            res[level - 1].append(node.val)
            dfs(node.left, level + 1, res)
            dfs(node.right, level + 1, res)

        res = []
        dfs(root, 1, res)
        return res
if __name__ == '__main__':
    pass 