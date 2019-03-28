#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@author: rye
#@time: 2019/3/28

'''
方法我感觉还算简单，但是实现起来花了一点时间，最后加了一段这个代码
        while q.next and q.next.val < x:
            q = q.next
            p = p.next
就pass了

实现比完美更重要，怎么简单怎么方便怎么来，现在还只是菜鸟，心态要easy
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if head == None:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        p, q = dummy, dummy
        while q.next and q.next.val < x:
            q = q.next
            p = p.next

        while q and q.next:
            if q.next.val < x:
                tmp_Node = ListNode(q.next.val)
                q.next = q.next.next
                tmp_Node.next = p.next
                p.next = tmp_Node
                p = p.next
                continue

            q = q.next

        return dummy.next.val

class Solution1(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head

        p1 = p2 = dummy

        while p1.next and p1.next.val < x:
            p1 = p1.next

        p2 = p1.next

        while p2:
            while p2.next and p2.next.val >= x:
                p2 = p2.next

            if p2.next == None:
                break
            node = p2.next
            p2.next = node.next
            node.next = p1.next
            p1.next = node
            p1 = p1.next

        return dummy.next

if __name__ == '__main__':
    # l1 = ListNode(1)
    # l1.next = ListNode(4)
    # l1.next.next = ListNode(3)
    # l1.next.next.next = ListNode(2)
    # l1.next.next.next.next = ListNode(5)
    # l1.next.next.next.next.next = ListNode(2)
    l1 = ListNode(3)
    l1.next = ListNode(1)
    l1.next.next = ListNode(2)

    print(Solution().partition(l1, 3))