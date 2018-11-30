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

if __name__ == '__main__':

    innum = "babad"
    innum1 = 'abbbb'

    print(Solution().longestPalindrome(innum1))