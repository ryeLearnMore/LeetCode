#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@author: rye
#@time: 2019/3/27

'''
可能做的题少，又把简单问题复杂化了。。。
自己写的代码跟大佬的代码相比不仅冗余，而且低效
'''

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
            return None

        dummy = ListNode(-1)
        dummy.next = head
        p, q = dummy, head
        flag = 0

        while q and q.next:
            while q.next and q.val == q.next.val:
                q = q.next
                flag = 1

            if flag == 1:
                q = q.next
                p.next = q
                if q and q.next and q.next.val != q.val:
                    p = q
                flag = 0
            elif p == q and q.next:
                q = q.next
            else:
                q = q.next
                p = p.next

        return dummy.next

# 大佬的代码
class Solution1(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        while head:
            if head.next and head.next.val == head.val: # 这一行和下一行的判断个人认为所是个技巧（取巧）
                while head.next and head.next.val == head.val:
                    head = head.next
                pre.next = head.next
                head = head.next
            else:
                pre = head
                head = head.next
        return dummy.next

if __name__ == '__main__':
    l1 = ListNode(-3)
    l1.next = ListNode(-3)
    l1.next.next = ListNode(-2)
    l1.next.next.next = ListNode(-1)
    l1.next.next.next.next = ListNode(-1)
    l1.next.next.next.next.next = ListNode(0)
    # l1 = ListNode(1)
    # l1.next = ListNode(1)
    print(Solution1().deleteDuplicates(l1))