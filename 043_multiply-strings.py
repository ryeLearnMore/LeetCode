#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@author: rye
#@time: 2019/3/12

'''
参考这两个链接就能明白这道题的核心（大数相乘）和方法了
https://zhuanlan.zhihu.com/p/42223805https://zhuanlan.zhihu.com/p/42223805
https://blog.csdn.net/weixin_41958153/article/details/80964818

解题思路：
两个字符串位数从右往左数，第一个数的第i位与第二个数的第j位相乘，会影响乘积的第i+j和第i+j-1位
'''

class Solution:
    # @param num1, a string
    # @param num2, a string
    # @return a string
    def multiply(self, num1, num2):
        #把num1,num2翻转方便计算
        num1 = num1[::-1]; num2 = num2[::-1]
        #每一位互相乘的结果用一维数组去储存
        arr = [0 for i in range(len(num1)+len(num2))]
        #填充这个一维数组
        for i in range(len(num1)):
            for j in range(len(num2)):
                arr[i+j] += int(num1[i]) * int(num2[j])
        ans = []
        #计算每一位的终极结果
        for i in range(len(arr)):
            #digit表示这一位的数字，  即i + j - 1位
            digit = arr[i] % 10
            #carry表示加给下一位的量， 即i + j位
            carry = arr[i] // 10
            if i < len(arr)-1:
                #下一位加上
                arr[i+1] += carry
            #更新答案
            ans.insert(0, str(digit))
        #去除首位为0的情况
        while ans[0] == '0' and len(ans) > 1:
            del ans[0]
        #连接成字符串
        return ''.join(ans)


# 按照理解自己写一遍
class Solution1:
    def multiply(self, num1, num2):
        num1 = num1[::-1]
        num2 = num2[::-1]
        temp_arr = [0 for i in range(len(num1) + len(num2))]
        for i in range(len(num1)):
            for j in range(len(num2)):
                temp_arr[i + j] += int(num1[i]) * int(num2[j])

        ans = []
        for i in range(len(temp_arr)):
            digital = temp_arr[i] % 10
            carry = temp_arr[i] // 10
            if i < len(temp_arr) - 1 :
                temp_arr[i + 1] += carry
            ans.insert(0, str(digital))

        while ans[0] == '0' and len(ans) > 1:
            del ans[0]
        return ''.join(ans)


if __name__ == '__main__':
    num1 = "123"
    num2 = "456"
    print(Solution1().multiply(num1, num2))