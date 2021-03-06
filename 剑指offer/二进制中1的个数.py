#!/usr/bin/env python
#coding:utf-8
#@author: rye
#@time: 2019/6/17 23:38

# 解题思路：
'''
如果一个整数不为0，那么这个整数至少有一位是1。如果我们把这个整数减1，
那么原来处在整数最右边的1就会变为0，原来在1后面的所有的0都会变成1(如果最右边的1后面还有0的话)。
其余所有位将不会受到影响。

举个例子：一个二进制数1100，从右边数起第三位是处于最右边的一个1。减去1后，第三位变成0，
它后面的两位0变成了1，而前面的1保持不变，因此得到的结果是1011.我们发现减1的结果是把最右边的
一个1开始的所有位都取反了。这个时候如果我们再把原来的整数和减去1之后的结果做与运算，从原来整
数最右边一个1那一位开始所有位都会变成0。如1100&1011=1000.也就是说，把一个整数减去1，再和原整
数做与运算，会把该整数最右边一个1变成0.那么一个整数的二进制有多少个1，就可以进行多少次这样的
操作。
'''

# 参考链接
'''
https://blog.csdn.net/fuxuemingzhu/article/details/79512764
https://www.nowcoder.com/profile/4627871/codeBookDetail?submissionId=8243218
'''
# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        # write code here
        cnt = 0
        if n < 0:
            n = n & 0xffffffff # python要使用n & 0xffffffff得到一个数的补码
        while n:
            cnt += 1
            n = n & (n - 1)
        return cnt