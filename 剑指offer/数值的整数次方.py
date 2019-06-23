#!/usr/bin/env python
#coding:utf-8
#@author: rye
#@time: 2019/6/19 23:26

# -*- coding:utf-8 -*-
class Solution:
    def Power(self, base, exponent):
        # write code here
        if base == 0:
            return False
        if exponent == 0:
            return 1
        flag = 1
        if exponent < 0:
            flag = -1
        result = 1
        for i in range(abs(exponent)):
            result *= base
        return result if flag > 0 else 1 / result