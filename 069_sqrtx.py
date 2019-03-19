#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@author: rye
#@time: 2019/3/19

'''
二分法。
当时没想到。
tips：
    注意return的条件
'''
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        # 作弊
        # return int(x ** (1 / 2))

        if x == 0:
            return 0
        if x == 1:
            return 1
        l, r = 0, x - 1
        while l <= r:
            # mid1 = l + (r - l) >> 1
            mid = l + ((r - l) >> 1)
            if mid ** 2 <= x and (mid + 1) ** 2 > x:
                return mid
            elif mid ** 2 > x:
                r = mid - 1
            else:
                l = mid + 1

if __name__ == '__main__':
    x = 3
    print(Solution().mySqrt(x))