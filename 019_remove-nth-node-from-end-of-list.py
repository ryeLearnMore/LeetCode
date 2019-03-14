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
这道题考的很简单，因为链表题刷的比较少，所以很不熟练。
tips:
1. 要自建头节点，即dumy节点，很重要
2. 指针的点要都在有效范围内，不要出去
'''
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        cnt = 0
        dumy = ListNode(0)
        dumy.next = head

        k = dumy
        while k.next:
            k = k.next
            cnt += 1
        step = cnt - n + 1

        cnt1 = 0
        l = dumy
        k = dumy.next
        while k:
            cnt1 += 1
            if cnt1 == step:
                l.next = k.next
                return dumy.next
            else:
                k = k.next
                l = l.next

# 大佬的做法：双指针（两个指纹始终保持恒定的间隔n，这样当后一个指针到末尾时，前一个指纹到达n）+头结点
class Solution1(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head
        p, q = dummy, dummy

        for i in range(n):
            q = q.next

        while q.next:
            p = p.next
            q = q.next

        p.next = p.next.next
        return dummy.next

if __name__ == '__main__':
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(3)
    l1.next.next.next = ListNode(4)
    l1.next.next.next.next = ListNode(5)
    n = 2
    print(Solution().removeNthFromEnd(l1, n))