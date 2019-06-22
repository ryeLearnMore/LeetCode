#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@author: rye
#@time: 2019/3/28

'''
头插法要断链。。。好久没做忘了
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        p = head
        prev = None
        while p:
            r = p.next
            p.next = prev
            prev = p
            p = r
        return prev


if __name__ == '__main__':
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(3)
    l1.next.next.next = ListNode(-1)
    l1.next.next.next.next = ListNode(-1)
    l1.next.next.next.next.next = ListNode(0)

    print(Solution().reverseList(l1))
    
# ------------------------------19.6.22-----------
'''
又在牛客网的“剑指offer”上做了一遍，结果不出意料的忘了。。。
要记住这个模式啊！！！
'''
