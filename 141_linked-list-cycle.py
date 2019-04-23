#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@author: rye
#@time: 2019/4/23

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow, fast = head, head
        if head == None:
            return False
        while fast.next != None and fast.next.next != None: # 因为如果是两个结点有环，则fast.next.next就不为空，而如果无环，则肯定false
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

# 法二
class Solution1(object):
    def hasCycle(self, head):
        """
                :type head: ListNode
                :rtype: bool
        """
        p1 = p2 = head
        while p2 and p2.pnext: #当链表为空或者只有一个结点时，就不执行循环体里的程序，返回False
            p1 = p1.pnext
            p2 = p2.pnext.pnext
            if p1 == p2:
                return True
        return False

if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node1.next = node2
    node2.next = node1
    print(Solution().hasCycle(node1))