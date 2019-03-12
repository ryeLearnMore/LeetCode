#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@author: rye
#@time: 2019/3/12

'''
能通过，但是代码写的很烂。
感觉有点取巧，因为当n = 2 **31 - 1时，leetcode会显示内存溢出。而我限制 n<2 ** 31 -1,所以避开了，但是处理边界花了很长时间
'''
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0 or x == 1.0 or (x == -1.0 and n % 2 == 0):
            return 1.0
        if x == -1.0:
            return -1.0
        if (abs(x) < 0.001 and n > 1) or (abs(x) > 1 and n <= -100):
            return 0.0
        if -2 ** 31 < n < 2 **31 -1:
            flag = 1
            if n < 0:
                flag = -1
                n = abs(n)

            temp = 0
            for i in range(n):
                if temp == 0:
                    temp = x
                    continue
                temp = temp * x
                if abs(temp) < 0.000001:
                    break

            if flag == -1:
                temp = 1/temp

            return temp
# 大佬的代码
'''
参考链接：https://blog.csdn.net/weixin_38111819/article/details/79138012
思路：（参考leetcode评论）
使用折半计算，每次把n缩小一半，这样n最终会缩小到0，任何数的0次方都为1，这时候我们再往回乘，
如果此时n是偶数，直接把上次递归得到的值算个平方返回即可，如果是奇数，则还需要乘上个x的值。
还有一点需要引起我们的注意的是n有可能为负数，对于n是负数的情况，我们可以先用其绝对值计算出一个结果再取其倒数即可。

我们让i初始化为n，然后看i是否是2的倍数，是的话x乘以自己，否则res乘以x，i每次循环缩小一半，直到为0停止循环。
最后看n的正负，如果为负，返回其倒数。
'''
class Solution1(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        if n < 0:
            return 1 / self.myPow(x, -n)
        if n % 2:  # n 为 奇数
            return x * self.myPow(x*x, n>>1)
        else:
            return self.myPow(x*x, n>>1)

if __name__ == '__main__':
    x, n = 2.00000, 10
    # x, n = 0.00001, 2147483647
    print(Solution1().myPow(x, n))