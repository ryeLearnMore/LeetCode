#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@author: rye
#@time: 2019/3/18

# 当初的想法和这个类似：https://blog.csdn.net/AosChen/article/details/79810348
# 就是用递归，结果又没跳出去那个固定的坑
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        def check(i, y, cnt):
            if i == m - 1 and y == n - 1:
                cnt += 1
                return cnt
            elif i < m - 1:
                # i += 1
                return check(i + 1, y, cnt)
            else:
                # y += 1
                return check(i, y + 1, cnt)
        return check(0, 0, 0)

'''
感想：
动态规划就是强，不能总是想着用递归解决这些问题了，因为递归复杂度太高，并不适合解决所有问题。
而且递归在return时跳不出去的坑还是没有理解。

方法：
    用一维数组代替了二维数据，涉及真的很巧妙，需要学习。
参考链接：https://github.com/ryeLearnMore/awesome-algorithm/blob/master/docs/Leetcode_Solutions/Python/062._unique_paths.md
'''
class Solution1:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m < 1 or n < 1:
            return 0
        dp = [0] *n
        dp[0] = 1
        for i in range(0,m):
            for j in range(1,n):
                dp[j] += dp[j-1]
        return dp[n-1]

if __name__ == '__main__':
    m = 7
    n = 3
    print(Solution1().uniquePaths(m, n))
