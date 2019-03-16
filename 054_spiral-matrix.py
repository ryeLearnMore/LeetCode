#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@author: rye
#@time: 2019/3/16

'''
这道题花了比较长的时间想，现在脑子有点晕
'''

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if matrix == []:
            return []
        res = []
        left = up = 0
        maxRight = len(matrix[0]) - 1
        maxDown = len(matrix) - 1
        direction = 0 # 0 is right, 1 is down, 2 is left, 3 up
        while True:
            if direction == 0:
                for i in range(left, maxRight + 1):
                    res.append(matrix[up][i])
                up += 1
            elif direction == 1:
                for i in range(up, maxDown + 1):
                    res.append(matrix[i][maxRight])
                maxRight -= 1
            elif direction == 2:
                for i in reversed(range(left, maxRight + 1)):
                    res.append(matrix[maxDown][i])
                maxDown -= 1
            else:
                for i in reversed(range(up, maxDown+1)):
                    res.append(matrix[i][left])
                left += 1
            if up > maxDown or left > maxRight:
                return res
            direction = (direction + 1) % 4

if __name__ == '__main__':
    matrix = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
    print(Solution().spiralOrder(matrix))