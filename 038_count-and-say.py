#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@author: rye
#@time: 2019/3/8

# 题都没看懂。。。看了好一会儿。
# 理解这道题，可以参考这个链接
# https://blog.csdn.net/weixin_41958153/article/details/80911011
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return '1'
        s = self.countAndSay(n-1) + '*'
        res, count = '', 1
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                count += 1
            else:
                res += str(count) + str(s[i])
                count = 1
        return res

if __name__ == '__main__':
    n = 4
    print(Solution().countAndSay(n))