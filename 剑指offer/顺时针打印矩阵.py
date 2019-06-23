#!/usr/bin/env python
#coding:utf-8
#@author: rye
#@time: 2019/6/23 16:58

# -*- coding:utf-8 -*-

'''
注意思想，重新做了一遍之后感觉没有那么难了，但是还没有独立做出来，需要多看！
'''
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        if matrix == []:
            return []
        res = []
        left = up = 0
        maxRight = len(matrix[0]) - 1
        maxDown = len(matrix) - 1
        direction = 0
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
                for i in range(maxRight, left - 1, -1):  # 注意这里该减了！
                    res.append(matrix[maxDown][i])
                maxDown -= 1
            elif direction == 3:
                for i in range(maxDown, up - 1, -1):  # 注意这里该减了！
                    res.append(matrix[i][left])
                left += 1
            if up > maxDown or left > maxRight:
                return res
            direction = (1 + direction) % 4

if __name__ == '__main__':
    matrix = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
    print(Solution().printMatrix(matrix))