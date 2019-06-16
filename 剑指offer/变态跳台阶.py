#!/usr/bin/env python
#coding:utf-8
#@author: rye
#@time: 2019/6/16 21:16

class Solution:
    def jumpFloorII(self, number):
        # write code here
        if number == 1:
            return 1
        if number == 2:
            return 2
        dp = [0] * number
        dp[0] = 1
        dp[1] = 2
        for i in range(2, number):
            dp[i] = sum(dp[:i]) + 1 # 此处必须加1，相当于从1阶台阶直接到n阶台阶
        return dp[-1]

# 这种在牛客网上看别人的答案，感觉像是找规律。。。
import math
class Solution1:
    def jumpFloorII(self, number):
        # write code here
        if number <= 0:
            return 0
        else:
            number = number - 1
            return math.pow(2,number)

if __name__ == '__main__':
    '''
    1 2 4
    '''
    number = 3
    print(Solution1().jumpFloorII(number))