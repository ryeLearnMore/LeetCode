#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@author: rye
#@time: 2019/3/29

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * n
        if n == 1:
            return 1
        elif n == 2:
            return 2
        for i in range(3, n + 1):
            dp[0] = 1
            dp[1] = 2
            dp[i - 1] = dp[i - 2] + dp[i - 3]

        return dp[-1]


if __name__ == '__main__':
    n = 3
    print(Solution().climbStairs(n))