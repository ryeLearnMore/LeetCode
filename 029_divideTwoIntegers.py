#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@author: rye
#@time: 2019/2/22
'''
总结：
1. 学习了两种0< a < b的比较
    if dividend < 0 < divisor or divisor < 0 < dividend:
    positive = (dividend < 0) is (divisor < 0)
2. 复习左移符号标志位<<和右移符号标志位>>的作用
3. 学习新的算不用除法做两个数整出的方法:减法和移位法
4. 学习len(range(start, stop, step))的用法和注意事项
'''
'''
方法一：用减法实现除法
python刷题实现甚至可以直接使用range()来实现除法，需要注意的点如下：

1.提前判断结果的正负号

2.结果在[-2**31，2**31-1]中，要判断结果是否移除

3.使用range()来计算除法时，一旦除法可以整除我们要对结果+1，因为len(range(3,7,3))的结果是2，len(range(3,9,3))的结果也是2

注：用while循环代替result = len(range(divisor, dividend, divisor))会超时，所以只能用这个len(range(a, b, c))
'''
class Solution1(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        below = 1
        if dividend < 0 < divisor or divisor < 0 < dividend:
            below = -1

        dividend, divisor = abs(dividend), abs(divisor)
        if dividend < divisor:
            return 0
        elif divisor == 1:
            result = dividend * below
            if result >= 2**31-1:
                return 2**31-1
            return result

        result = len(range(divisor, dividend, divisor))
        if (result+1) * divisor == dividend:
            result += 1
        return result * below
'''
用位运算，运用二分的思想

因为最坏的情况就是最大的数除以1，即2**31 / 1, 所以时间复杂度就是O(1)，如果assuming n is the number of bits， 那就是O(lgN)

思路总结：
总的来说，这思路就是不断将dividend减少的while循环。总体循环分两层。外层用来控制最终跳出循环情况，
同时它可以初始化逼近的间隔。内层是用来加快逼近速度的，你可以看到它是不断的2倍2倍的翻。
所以总体思路和我一开始叠加的想法差不多，只不过它用了逼近的方法去提高自己的效率。所以这也是一种二分查找。
--------------------- 
作者：weixin_41958153 
来源：CSDN 
原文：https://blog.csdn.net/weixin_41958153/article/details/80797415 
版权声明：本文为博主原创文章，转载请附上博文链接！
'''
# 用到的点：
'''
1. is 和 ==
在 Python 中会用到对象之间比较，可以用 ==，也可以用 is 。但是它们的区别是什么呢？

is 比较的是两个实例对象是不是完全相同，它们是不是同一个对象，占用的内存地址是否相同。莱布尼茨说过：“世界上没有两片完全相同的叶子”，这个is正是这样的比较，比较是不是同一片叶子（即比较的id是否相同，这id类似于人的身份证标识）。

== 比较的是两个对象的内容是否相等，即内存地址可以不一样，内容一样就可以了。这里比较的并非是同一片叶子，可能叶子的种类或者脉络相同就可以了。默认会调用对象的 __eq__()方法。

2. <<左移运算符 和 >>右移运算符
若a = 60
<<	左移动运算符：
运算数的各二进位全部左移若干位，由 << 右边的数字指定了移动的位数，高位丢弃，低位补0。	
a << 2 输出结果 240 ，二进制解释： 1111 0000
>>	右移动运算符：把">>"左边的运算数的各二进位全部右移若干位，>> 右边的数字指定了移动的位数	
a >> 2 输出结果 15 ，
'''

class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        #首先这一句就很python，postive 为true是符号相同
        positive = (dividend < 0) is (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        #检查dividend是否大于divisor
        #如果还小于则进行小精度的逼近dividend
        while dividend >= divisor:
            temp, i = divisor, 1
            #增大逼近dividend的步伐
            #i不断增加， temp不断减少
            while dividend >= temp:
                #经过上一句的判断，所以dividend还大于0
                dividend -= temp
                #商要加对应的i
                res += i
                #倍数相应的要增加
                i = i<<1
                #目前的值也要不断的增加
                temp = temp<<1
        #判定正负号
        if not positive:
            res = -res
        return min(max(-2147483648,res), 2147483647)

# 重写一遍用减法
'''
仿照方法一的思路写了一个，但是运行到dividend = 2147483647，divisor = 2发现超时，所以还得用len(range())
'''
class Solution2:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        flag = 1
        if (divisor < 0 and dividend > 0) or (dividend < 0 and divisor > 0):
            flag = -1

        res = 0

        divisor, dividend = abs(divisor), abs(dividend)
        if divisor > dividend:
            return 0
        if divisor == 1:
            result = dividend * flag
            if result >= 2**31 - 1:
                return 2**31 - 1
            else:
                return result

        while dividend >= divisor:
            dividend -= divisor
            res += 1
        return flag * res


if __name__ == '__main__':
    dividend = 2147483647
    divisor = 2
    print(Solution2().divide(dividend, divisor))