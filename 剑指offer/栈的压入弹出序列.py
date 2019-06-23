#!/usr/bin/env python
#coding:utf-8
#@author: rye
#@time: 2019/6/23 18:25

# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        if not pushV or len(pushV) != len(popV):
            return False
        stack = []
        for i in pushV:
            stack.append(i)
            while len(stack) and stack[-1] == popV[0]:
                stack.pop(-1)
                popV.pop(0)
        if len(stack):
            return False
        return True