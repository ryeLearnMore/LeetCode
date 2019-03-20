#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@author: rye
#@time: 2019/3/20
'''
刚开始题没看懂，又读了几遍大致懂了。
参考评论的写法自己写的。

本体属于二分法的应用，此次是应用到二维矩阵中，
法一属于利用二分法的思想，结合该二维矩阵的特点，灵活使用的二分法。与法二相比更加灵活。
'''
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        row = len(matrix)
        if row == 0: # 注意排除matrix为空的情况。
            return False
        else:
            col = len(matrix[0])

        l = 0
        r = -1

        while l < row and r >= -col:
            point = matrix[l][r]
            if point == target:
                return True
            elif point < target:
                l += 1
            else:
                r -= 1
        return False

'''
真正的二分法。
'''
class Solution1(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        row = len(matrix)
        col = len(matrix[0]) if row else 0
        l, r = 0, row - 1
        while l <= r:
            mid_row = l + ((r - l) >> 2)
            if matrix[mid_row][0] <= target <= matrix[mid_row][-1]:
                m, n = 0, col - 1
                while m <= n:
                    mid_col = m + ((n - m) >> 2)
                    if matrix[mid_row][mid_col] > target:
                        n = mid_col - 1
                    elif matrix[mid_row][mid_col] < target:
                        m = mid_col + 1
                    else:
                        return True
                return False
            elif target < matrix[mid_row][0]:
                r = mid_row - 1
            else:
                l = mid_row + 1
        return False

if __name__ == '__main__':
    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ]
    target = 13
    print(Solution().searchMatrix(matrix, target))