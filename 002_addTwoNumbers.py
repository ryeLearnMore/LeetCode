#-*-coding:utf-8-*- 
__author__ = 'Rye'


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    # __repr__
    # https: // blog.csdn.net / luckytanggu / article / details / 53649156
    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, self.next)

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        root = ListNode(0)
        current = root

        val, carry = 0, 0
        while l1 or l2 or carry:
            val = carry
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next
            # divmod()
            # http: // www.runoob.com / python / python - func - divmod.html
            carry, val = divmod(val, 10)
            current.next = ListNode(val)
            current = current.next

        if carry == 1:
            current.val = ListNode(1)
        return root.next

if __name__ == '__main__':
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    print(Solution().addTwoNumbers(l1, l2))









