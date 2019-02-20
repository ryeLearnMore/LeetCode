#!/usr/bin/env python
#coding:utf-8
#@author: rye
#@time: 2019/2/20 10:58

'''
此题貌似被人一直吐槽。看到有评论可以用一行代码解决：print(haystack.find(needle))
tips：
1. if ‘’ in haystack是可以被找到的，找到的下标为0！一定要记住!
2. 所以当needle为空时，无论haystack是什么都可以被找到，找到的下标都为0
'''
# 我是用切片做的
# 其他解法可以看这里：https://github.com/ryeLearnMore/awesome-algorithm/blob/master/docs/Leetcode_Solutions/Python/028._implement_strstr().md
class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle in haystack and needle != '':
            for i in range(len(haystack)):
                if needle[0] == haystack[i]:
                    if needle == haystack[i:i + len(needle)]:
                        return i
        elif needle == '':
            return 0
        else:
            return -1


if __name__ == '__main__':
    haystack = "ab"
    needle = "c"
    print(Solution().strStr(haystack, needle))