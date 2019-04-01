#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@author: rye
#@time: 2019/4/1


# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
'''
用的是和116题一样的代码，也通过了，因为方法是层次遍历 + 插入节点，不过时间和内存很差
'''
class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        res = []

        if not root:
            return None
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
                tmp.append(r)
            res.append(tmp)

        for cur_level in res:
            for i in range(len(cur_level)-1):
                cur_level[i].next = cur_level[i+1]

        return root

# 大佬的代码，迭代版本
'''
说实话，看的不是很懂，日后再看看，今天是2019.4.1
'''
class Solution1:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        prev = None
        head = None
        cur = root
        while (cur != None):
            while (cur != None):
                if cur.left:
                    if prev:
                        prev.next = cur.left
                    else:
                        head = cur.left
                    prev = cur.left

                if cur.right:
                    if prev:
                        prev.next = cur.right
                    else:
                        head = cur.right
                    prev = cur.right
                cur = cur.next
            cur = head
            prev = None
            head = None

if __name__ == '__main__':
    pass 