#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@author: rye
#@time: 2019/3/31

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
'''
写的过程中，将root.left = sortedArrayToBST(list[:mid])中的sortedArrayToBST写成TreeNode。。。
还是有点马虎。

总结：
    学会利用将难题转化为已知的题。
'''
class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        def sortedArrayToBST(list):
            if not list:
                return None
            else:
                mid = len(list) // 2
                root = TreeNode(list[mid])
                root.left = sortedArrayToBST(list[:mid])
                root.right = sortedArrayToBST(list[mid + 1:])
                return root
        if not head:
            return None
        else:
            res = []
            while head:
                res.append(head.val)
                head = head.next
            return sortedArrayToBST(res)
# 自己写的，未通过（超时）
'''
利用上一题的思想，每次递归都遍历链表，寻找中间节点，但是很麻烦，看了答案之后，发现只需要将链表转化为数组就行。。。
'''
class Solution1(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        length = 0
        p = head
        while p:
            length += 1
            p = p.next
        mid = length // 2

        cnt = 0
        p = head
        while cnt <= mid:
            cnt += 1
            p = p.next

        if not p:
            return
        q = p.next
        p.next = None

        root = TreeNode(p.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(q)
        return root

if __name__ == '__main__':
    pass 