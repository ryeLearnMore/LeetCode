#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@author: rye
#@time: 2019/3/27

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return head

        dummy = ListNode(-1)
        dummy.next = head
        q = dummy
        if q.next:
            q = q.next
        while q and q.next:
            if q.val == q.next.val:
                q.next = q.next.next
            else:
                q = q.next

        return dummy.next.val
        # while q.next:
        #     q = q.next
        #     while q.next:
        #         if q.val == q.next.val:
        #             q = q.next
        #         else:
        #             p = q

# 大佬的代码
class Solution1(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        curr = head

        while curr:
            while curr.next:
                if curr.val == curr.next.val:
                    curr.next = curr.next.next
                else:
                    break

            curr = curr.next
        return head

if __name__ == '__main__':
    l1 = ListNode(1)
    l1.next = ListNode(1)
    l1.next.next = ListNode(1)
    # l1.next.next.next = ListNode(3)
    # l1.next.next.next.next = ListNode(3)
    print(Solution().deleteDuplicates(l1))