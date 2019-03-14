#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@author: rye
#@time: 2019/3/14

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

'''
解题思路：
1. 先用链表删除的方法，然后用插入的方法，插入节点
2. 用三个指针，且三个指针的要想清楚，不能搞乱
'''


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dumy = ListNode(-1)
        dumy.next = head
        p = dumy

        while p.next and p.next.next:
            q, r = p.next, p.next.next
            q.next = r.next
            r.next = q
            p.next = r

            p = q

        return dumy.next

if __name__ == '__main__':
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(3)
    l1.next.next.next = ListNode(4)

    print(Solution().swapPairs(l1))