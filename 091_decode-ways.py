#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@author: rye
#@time: 2019/3/25

'''
tag:dp
解题思路:
https://github.com/apachecn/awesome-algorithm/blob/master/docs/Leetcode_Solutions/Python/0091._decode_ways.md

开始有考虑用dp，但是尝试算了一下，感觉不对，后来没思路看了答案，发现是dp。。。
个人感觉这道题算dp中比较难的
tips：
1. 0的考虑
2. dp[0],dp[1]的考虑
3. 判断 dp[i] 时，它有两种可能的组合方式：
    1). 自身解码
        - 如果当前字符不是'0'，那么dp[i]的组合可以为dp[i-1]的所有组合方式后面都加上当前字符
        - 如果当前字符是'0'，那么dp[i]在这种情况下没有符合的组合方式
    2). 和它前面的一个字符一起解码
        - 如果10 <= int(s[i-1:i+1]) <= 26, 那么dp[i]的组合可以为dp[i-2]的所有组合方式后面都加上s[i-1:i+1]
        - 如果int(s[i-1:i+1]) < 10 或者 int(s[i-1:i+1]) > 26，那么dp[i]在这种情况下没有符合的组合方式
'''

# -------------------------------19.4.6--------------------------------
'''
看这三个参考链接就能看懂，结合爬楼梯那道题
https://www.cnblogs.com/racaljk/p/8454243.html
https://blog.csdn.net/qqxx6661/article/details/78389583
https://github.com/apachecn/awesome-algorithm/blob/master/docs/Leetcode_Solutions/Python/0091._decode_ways.md
'''
# 个人觉得下面这段代码更好理解
class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = [0] * (len(s)+1)
        #边界情况
        if len(s) == 0 or s[0] == '0':
            return 0
       
        dp[0] = 1
        dp[1] = 1
        for i in range(2,len(s) + 1):
            if s[i-1] > '0':  #若s[i-1]不为0,则s[i-1]可单独存在,s[i]可由s[i-1]走1步到达
                dp[i] = dp[i-1]
            if s[i-2] == '1' or (s[i-2] == '2' and s[i-1] <= '6') : #承接上面，若s[i-2]*10+s[i-1]<=26,则s[i]可由s[i-2]走2步到达
                dp[i] += dp[i-2]
        return dp[len(s)]
# --------------------- 
# 作者：Yun_Self 
# 来源：CSDN 
# 原文：https://blog.csdn.net/u014626513/article/details/81483008 
# 版权声明：本文为博主原创文章，转载请附上博文链接！
# ---------------------------------------------19.4.6------------------------
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or len(s) == 0:
            return 0
        if len(s) == 1 and s[0] == '0':
            return 0
        elif len(s) == 1 and s[0] != '0':
            return 1

        dp = [0] * len(s)
        dp[0] = 1 if s[0] != '0' else 0

        if 10 <= int(s[:2]) <= 26:
            if s[1] == '0':
                dp[1] = 1
            else:
                dp[1] = 2
        else:
            if s[1] == '0':
                dp[1] = 0
            else:
                dp[1] = dp[0]
        for i in range(2, len(s)):
            if s[i] != '0':
                dp[i] += dp[i - 1]
            if 10 <= int(s[i - 1:i + 1]) <= 26:
                dp[i] += dp[i - 2]
        return dp[-1]


class Solution1(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or len(s) == 0:
            return 0
        if len(s) == 1 and s[0] == '0':
            return 0
        elif len(s) == 1 and s[0] != '0':
            return 1

        dp = [0] * len(s)
        dp[0] = 1 if s[0] != '0' else 0

        if 10 <= int(s[:2]) <= 26:
            if s[1] == '0':
                dp[1] = 1
            else:
                dp[1] = 2
        else:
            if s[1] == '0':
                dp[1] = 0
            else:
                dp[1] = dp[0]
            # dp[1] = 0 # 反例：‘27’

        for i in range(2, len(s)):
            if s[i] != '0':
                dp[i] += dp[i - 1]
            if 10 <= int(s[i - 1:i + 1]) <= 26:
                dp[i] += dp[i - 2]

        return dp[-1]


if __name__ == '__main__':
    s = "02"
    print(Solution1().numDecodings(s))
