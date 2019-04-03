#!/user/bin/env python
# *v* coding:utf-8 *v*
#@time:2018/11/30 9:30
#@author:rye

# 参考：https://github.com/apachecn/awesome-algorithm/blob/master/docs/Leetcode_Solutions/Python/005._longest_palindromic_substring.md
# 中的算法二
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        length = len(s)
        l, r, m = 0, 0, 0

        for i in range(0, length):
            # 若有奇数个回文子串
            for j in range(min(i + 1, length - i)):
                if s[i - j] != s[i + j]:
                    break
                if 2 * j + 1 > m:
                    m = 2 * j + 1
                    l = i - j
                    r = i + j
            # 若有偶数个回文子串，需往前多算一个
            if i + 1 < length and s[i] == s[i + 1]:
                for j in range(min(i + 1, length - i - 1)):
                    if s[i - j] != s[i + j + 1]:
                        break
                    if 2 * j + 2 > m:
                        m = 2 * j + 2
                        l = i - j
                        r = i + j + 1

        return s[l: r + 1]
# ------------------------19.4.3------------------------------------
'''
第一种思路:
以每个字母为回文中心,考虑回文长度为奇数和偶数的情况.

第二种思路:
以每个字母为回文串的结束标志,分别考虑可能回文为奇数和偶数的情况.

第三种思路:
令dp[j][i]从字符串j到i是否为回文串
动态回归方程 dp[j][i]是看j+1和i-1是否为回文串.
'''

# 第一种思路
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        self.start = 0
        self.max_len = 0
        n = len(s)
        if n < 2:
            return s

        def helper(i, j):
            while i >= 0 and j < n and s[i] == s[j]:
                i -= 1
                j += 1

            if self.max_len < j - i - 1:
                # print(i,j)
                self.max_len = j - i - 1
                self.start = i + 1

        for k in range(n):
            #print(k)
            helper(k, k)
            helper(k, k + 1)
        return s[self.start:self.start + self.max_len ]

# 第二种思路
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        if n < 2 or s == s[::-1]:
            return s
        max_len = 1
        start = 0
        for i in range(1,n):
            even = s[i-max_len:i+1]
            odd = s[i-max_len-1:i+1]
            if i-max_len-1>=0 and odd == odd[::-1]:
                start = i-max_len-1
                max_len += 2
                continue
            if i-max_len>=0 and even == even[::-1]:
                start = i-max_len
                max_len += 1
        return s[start:start+max_len]

# 第三种思路
class Solution(object):
    def longestPalindrome(self, s):
    	 n = len(s)
        dp = [[0] * n for _ in range(n)]
        max_len = float("-inf")
        res = ""
        for i in range(n):
            # dp[i][i] = 1
            for j in range(i, -1, -1):
                if s[i] == s[j] and (i - j < 2 or dp[i - 1][j + 1]):
                    dp[i][j] = 1

                if dp[i][j] and i - j + 1 > max_len:
           
                    max_len = i - j + 1
                    res = s[j:i + 1]
        # print(dp)
        return res
# ------------------------19.4.3------------------------------------
if __name__ == '__main__':

    innum = "babad"
    innum1 = 'abbbb'

    print(Solution().longestPalindrome(innum1))
