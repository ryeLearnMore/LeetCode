#!/usr/bin/env python
#coding:utf-8
#@author: rye
#@time: 2019/6/16 20:38

# -*- coding:utf-8 -*-

# 斐波那契数列可实现的五种方法
# https://www.cnblogs.com/panlq/p/9307203.html
class Solution:
    def Fibonacci(self, n):
        # write code here
        if n == 1 or n == 0:
            return n
        if n == 2:
            return 1
        else:
            dp = [0] * (n + 1)
            a = dp[0] = 0
            b = dp[1] = 1
            for i in range(2, n + 1):
                dp[i] = a + b
                a = b
                b = dp[i]
            print(dp)
            return dp[-1]

if __name__ == '__main__':
    n = 3
    print(Solution().Fibonacci(n))