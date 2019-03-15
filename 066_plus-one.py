#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@author: rye
#@time: 2019/3/15

'''
这道简单题想复杂了，没有好好考虑利用list的特性，所以有点失败。
'''
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        nums = 0
        for i in range(len(digits)):
            nums += digits[i] * 10 ** (len(digits) - i - 1)
        nums += 1

        # res = []
        # while nums != 0:
        #     length = len(str(nums))
        #     res.append(nums // (10 ** (length - 1)))
        #     nums = nums % (10 ** (length - 1))
        #     while length - len(str(nums)) > 1:
        #         res.append(0)
        #         length -= 1
        #
        # return res
        return [int(x) for x in str(nums)]

# 解法二：递归
class Solution1(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if digits == []:
            return [1]
        if digits[-1] < 9:
            return digits[:-1] + [digits[-1] + 1]
        else:
            return self.plusOne(digits[:-1]) + [0]

if __name__ == '__main__':
    nums = [1,2,3]
    nums1 = [9,9]
    nums2 = [1,0,0,0,0]
    print(Solution1().plusOne(nums1))