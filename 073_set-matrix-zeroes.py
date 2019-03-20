#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@author: rye
#@time: 2019/3/20

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        row = len(matrix)
        col = len(matrix[0])

        res = []
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    res.append([i, j])
        for k in res:
            for k1 in range(col):
                matrix[k[0]][k1] = 0
            for k2 in range(row):
                matrix[k2][k[1]] = 0

        return matrix

# 大佬的代码
'''
思想：https://github.com/ryeLearnMore/awesome-algorithm/blob/master/docs/Leetcode_Solutions/Python/073.%20Set%20Matrix%20Zeroes.md
一边遍历，一边将相应的行和列置为0是行不通的，会影响后面元素的遍历判断，
所以要记录下哪些行和哪些列是要置为0的。为了节约空间，在原矩阵中借两条边，如果该行或者列要置为0，
则把左边或者上边的相应位置置为0。如果左边和上边本来就有0，那么需要额外标记一下，最后把左边或者右边也全部置为0.
'''
class Solution1(object):
    def setZeroes(self, matrix):
        if len(matrix) == 0:
            return

        colFlag, rowFlag, rows, cols = 1, 1, len(matrix), len(matrix[0])

        # Recording whether the first row and the first col contain 0
        for i in range(cols):
            if matrix[0][i] == 0:
                colFlag = 0

        for i in range(rows):
            if matrix[i][0] == 0:
                rowFlag = 0

        # Start from the second row and the second col
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0

        # Set zero from the bottom
        for i in range(rows - 1, 0, -1):
            for j in range(cols - 1, 0, -1):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Check the row and the col
        if colFlag == 0:
            for i in range(cols):
                matrix[0][i] = 0
        if rowFlag == 0:
            for i in range(rows):
                matrix[i][0] = 0

if __name__ == '__main__':
    matrix = [
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]
    ]
    print(Solution().setZeroes(matrix))