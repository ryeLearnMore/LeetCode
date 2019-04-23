#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@author: rye
#@time: 2019/4/23

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# 参考链接，很容易理解
# https://blog.csdn.net/sinat_35261315/article/details/79205157
class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        hasCycle = False
        p, q = head, head
        if not p or not p.next:
            return None

        while q.next and q.next.next:
            p = p.next
            q = q.next.next
            if p == q:
                hasCycle = True
                break

        if hasCycle == True:
            p = head
            while p != q:
                p = p.next
                q = q.next
            return p
        return None

if __name__ == '__main__':
    pass 