#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@author: rye
#@time: 2019/3/14

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dumy = ListNode(-1)
        d = dumy

        p = l1
        q = l2

        while p and q:
            if p.val <= q.val:
                d.next = p
                p = p.next
                d = d.next
            else:
                d.next = q
                q = q.next
                d = d.next
        if p:
            d.next = p
        if q:
            d.next = q
        return dumy.next

if __name__ == '__main__':
    pass 