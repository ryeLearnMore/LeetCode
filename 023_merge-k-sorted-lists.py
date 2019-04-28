#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@author: rye
#@time: 2019/4/28


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# 法一：笨法，不断调用两个链表融合，多次执行。不过方法虽然看起来笨一点，但是总比什么都写不上强。
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if lists == []:
            return []
        L = len(lists)
        res = lists[0]
        for i in range(1, L):
            res = self.mergeTwoLists(res, lists[i])

        return res

    def mergeTwoLists(self, l1, l2):
        ans = ListNode(0)
        res = ans
        while l1 and l2:
            if l1.val < l2.val:
                res.next = l1
                res = res.next
                l1 = l1.next
            else:
                res.next = l2
                res = res.next
                l2 = l2.next

        if l1:
            res.next = l1
        if l2:
            res.next = l2
        return ans.next

class Solution1(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        heap = []
        import heapq
        for node in lists:
            if node:
                heap.append((node.val, node))  # 堆中放入tuple：值，地址
        heapq.heapify(heap)  # 做成堆
        dummy = ListNode(0)
        curr = dummy

        while heap:
            pop = heapq.heappop(heap)  # 从堆中取最小的值
            curr.next = ListNode(pop[0])  # 将值放入
            curr = curr.next
            if pop[1].next:  # 如果该链表没结束
                heapq.heappush(heap, (pop[1].next.val, pop[1].next)) # 将该链表下个节点压入栈中
        return dummy.next
# ---------------------
# 作者：Rude3knife
# 来源：CSDN
# 原文：https://blog.csdn.net/qqxx6661/article/details/77814794
# 版权声明：本文为博主原创文章，转载请附上博文链接！

# 法3 用这个最取巧了！
class Solution3(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        nlist=[]
        for node in lists:
            while(node):
                nlist.append(node.val)
                node=node.next
        nlist.sort()
        head=ListNode(None)
        temp=head
        for i in nlist:
            temp.next=ListNode(i)
            temp=temp.next
        return head.next

if __name__ == '__main__':
    pass