#!/usr/bin/env python
#coding:utf-8
#@author: rye
#@time: 2019/6/16 22:27

# 参考链接：
'''
https://blog.csdn.net/u010005281/article/details/79849924
https://www.jb51.net/article/140446.htm 这条链接告诉我们：跳台阶、变态跳台阶、矩形覆盖其实都和斐波那契数列是一类问题
http://www.pianshen.com/article/5637309798/
'''

# 注：跳台阶、变态跳台阶、矩形覆盖其实都和斐波那契数列是一类问题
class Solution:
    def rectCover(self, number):
        # write code here
        if number <= 0:
            return 0
        a = 1
        b = 2
        while number > 1:
            a, b = b, a + b
            number -= 1
        return a
if __name__ == '__main__':
    number = 2
    print(Solution().rectCover(number))
    # print(math.pow(2, 2)) # 4.0