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
我的方法：
层次遍历 + 插入next指针
还是大佬的方法好，具体看大佬的注释
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

# 大佬的代码
class Solution1:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        # 看了下速度最快的代码，实现思路和我的层次遍历不一样
        # 那份代码本质上也是层次遍历，但实现思路上更加巧妙，且浪费的空间更少
        # 下面代码是那份参考代码
        if not root:
            return
        prev = root  # 用prev来记录每一行的头节点
        while prev.left:
            current = prev  # 用current对每一行进行遍历
            # 每一行的遍历是利用了next属性，避免了（传统层次遍历方法）从队列中弹出节点，节约了时间
            while current:
                current.left.next = current.right
                if current.next:
                    current.right.next = current.next.left
                current = current.next
            prev = prev.left
if __name__ == '__main__':
    pass 