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
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        if not root:
            return res
        flag = 1
        queue = []
        queue.append(root)
        while len(queue) != 0:
            tmp = []
            for i in range(len(queue)):
                p = queue.pop(0)
                if p.left:
                    queue.append(p.left)
                if p.right:
                    queue.append(p.right)
                tmp.append(p.val)
            flag = -1 * flag
            if flag == -1:
                res.append(tmp)
            else:
                # res.append(tmp[::-1])
                res.append(reversed(tmp))
        return res

# 可能这题考点时非递归层次遍历的写法。最后需要讲res中的偶数下表反转一下
class Solution1(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        _r = []
        if not root:
            return _r

        _q = []
        _q.append(root)

        while _q:
            tmp = []

            for i in range(len(_q)):
                _c = _q.pop(0)
                tmp.append(_c.val)

                if _c.left:
                    _q.append(_c.left)
                if _c.right:
                    _q.append(_c.right)

            _r.append(tmp)

        for index, elem in enumerate(_r):
            if index % 2:
                _r[index].reverse()
        return _r

if __name__ == '__main__':
    pass 