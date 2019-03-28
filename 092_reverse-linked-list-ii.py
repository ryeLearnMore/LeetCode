#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@author: rye
#@time: 2019/3/28

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
'''
思路：用三个指针，先找第m - 1个节点，然后按照头插法逆序插入。
'''
class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        cnt = 0
        dummy = ListNode(-1)
        dummy.next = head
        p, q, r = dummy, head, dummy
        while q:
            cnt += 1
            if cnt == m - 1:
                r = q
                q = q.next
                p = p.next
            elif m < cnt <= n:
                p.next = p.next.next
                q.next = r.next
                r.next = q
                q = p.next
            else:
                p = p.next
                q = q.next
        return dummy.next

if __name__ == '__main__':
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(3)
    l1.next.next.next = ListNode(4)
    l1.next.next.next.next = ListNode(5)
    l1.next.next.next.next.next = ListNode(0)
    print(Solution().reverseBetween(l1, 2, 4))