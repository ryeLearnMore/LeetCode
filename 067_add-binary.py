#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@author: rye
#@time: 2019/3/16
'''
这道题我感觉跟66题有点像，一下想到是不是可以用递归解决，尝试了一下，成功了。貌似还没看到这样的解法或是我没找到。
tips:
真的要自己亲手实现一下才会注意到看不见的细节。通常递归后面要加一个固定值，而不能总是return f().
'''
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        sum_ = int(a) + int(b)
        strS = str(sum_)

        def check(strs):
            if strs == '':
                return ''
            if strs[-1] == '2' and len(strs) != 1:
                # strs = strs.replace(strs[-1], '0')
                newStr = str(int(strs[:-1]) + 1)
                #
                # if len(newStr) == 1:
                #     return '10'
                # else:
                #     return check(newStr) + '0'
                return check(newStr) + '0'
            if strs[-1] == '3' and len(strs) != 1:
                newStr = str(int(strs[:-1]) + 1)
                return check(newStr) + '1'
            elif strs == '2':
                return '10'
            elif strs == '3':
                return '11'
            else:
                return check(strs[:-1]) + strs[-1]

        return check(strS)

if __name__ == '__main__':
    a = "11"
    b = "1"
    a1 = "1010"
    b1 = "1011"
    a2 = "1111"
    b2 = "1111"
    print(Solution().addBinary(a2, b2))