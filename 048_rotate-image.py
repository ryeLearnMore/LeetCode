#!/usr/bin/env python
#coding:utf-8
#@author: rye
#@time: 2019/3/1 20:11

# 此题没想出来
'''
tips:
1. 这种题就属于想不出来就真不会做，看一眼答案就知道方法了。
2.
temp = x
x = y        ==     x, y = y, x      这种交换变量不需要temp，可以直接交换，算是python特有吧
y = temp
'''
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        n = len(matrix)
        # 上下翻转
        for i in range(n // 2):
            matrix[i], matrix[n - 1 - i] = matrix[n - 1 - i], matrix[i]
        # 主对角线翻转
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        return matrix

if __name__ == '__main__':
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print(Solution().rotate(matrix))