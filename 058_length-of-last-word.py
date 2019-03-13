#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@author: rye
#@time: 2019/3/13

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == '':
            return 0
        s = s.strip(' ')
        if ' ' in s:
            for i in range(len(s) - 1, -1, -1):
                if s[i] == ' ':
                    return len(s[i + 1:])
        else:
            return len(s)

# 大佬做法，很有趣
class Solution1(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s[::-1].strip()
        return s.find(' ') if s.find(' ') != -1 else len(s)

if __name__ == '__main__':
    s = "Hello"
    s1 = "a "
    print(Solution().lengthOfLastWord(s1))