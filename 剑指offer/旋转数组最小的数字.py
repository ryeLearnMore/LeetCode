#!/usr/bin/env python
#coding:utf-8
#@author: rye
#@time: 2019/6/15 17:56

# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if len(rotateArray) == 0:
            return 0
        l = 0
        r = len(rotateArray) - 1
        while l <= r:
            mid = l + (r - l) // 2
            #if l == r:
            if r - l == 1:
                return rotateArray[r]
                return rotateArray[l] if rotateArray[l] < rotateArray[r] else rotateArray[r]
            elif rotateArray[l] <= rotateArray[mid]:
                 l= mid
            else:
                r = mid