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
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None or k == 0:
            return head

        dumy = ListNode(-1)
        dumy.next = head
        p = dumy
        q = dumy
        length = 0
        cnt = 0
        # 真的不懂这个while循环怎么就超时了
        while q.next:
            length += 1
            q = q.next

        k = k % length

        q = dumy
        while q.next:
            if cnt < k:
                cnt += 1
            else:
                p = p.next
            q = q.next

        q.next = dumy.next
        dumy.next = p.next
        return dumy.next


class Solution1(object):
    def rotateRight(self, head, k):
        if head == None or k == 0:
            return head

        cur = head
        size = 1
        while cur.next:
            size += 1
            cur = cur.next

        tail = cur

        k = k % size

        p = self.findKth(head, k)

        tail.next = head
        head = p.next
        p.next = None
        return head

    def findKth(self, head, k):
        dummy = ListNode(-1)
        dummy.next = head
        p = dummy
        q = dummy

        for i in range(k):
            q = q.next

        while q.next:
            p = p.next
            q = q.next
        return p


if __name__ == '__main__':
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(3)
    l1.next.next.next = ListNode(4)
    l1.next.next.next.next = ListNode(5)

    print(Solution().rotateRight(l1, 2))