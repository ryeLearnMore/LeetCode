#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@author: rye
#@time: 2019/3/18
'''
本题和54题属于一个思路，当时感觉有点懵，自己按照那个题的思路写了一下发现不对。后又重写一遍，
感觉真的有点理解了。看来第一遍还是应该快速浏览，重点放在第二遍和第三遍才能更深体会算法的思想。
'''
# 本想自己写，但是发现失败了。
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        martix = [[] for i in range(n)]
        for i in range(n ** 2):
            if i // n <= n:
                martix[i // n].append(-1)

        i, j, idx = 0, 0, 1

        direction = 0

        while idx <= n ** 2:
            if direction == 0: # to right
                while j < n:
                    martix[i][j] = idx
                    j += 1
                    idx += 1
                j -= 1
                i += 1
            if direction == 1: # to down
                while i < n:
                    martix[i][j] = idx
                    i += 1
                    idx += 1
                i -= 1
                j -= 1
            if direction == 2: # to left
                while j >= 0:
                    martix[i][j] = idx
                    j -= 1
                    idx += 1
                j += 1
                i -= 1
            if direction == 3: # to up
                while j >= 0:
                    martix[i][j] = idx
                    j -= 1
                    idx += 1

            direction += 1
            direction = direction % 4

        return martix

# 按照54题思路重写的。
class Solution1(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        martix = [[] for i in range(n)]
        for i in range(n ** 2):
            if i // n <= n:
                martix[i // n].append(-1)

        maxUp, maxLeft, idx = 0, 0, 0
        maxDown = maxRight = n - 1

        direction = 0

        while 1:
            if direction == 0: # to right
                for i in range(maxLeft, maxRight + 1):
                    idx += 1
                    martix[maxUp][i] = idx
                maxUp += 1
            if direction == 1: # to down
                for i in range(maxUp, maxDown + 1):
                    idx += 1
                    martix[i][maxRight] = idx
                maxRight -= 1
            if direction == 2: # to left
                for i in range(maxRight, maxLeft - 1, -1):
                    idx += 1
                    martix[maxDown][i] = idx
                maxDown -= 1
            if direction == 3: # to up
                for i in range(maxDown, maxUp - 1, -1):
                    idx += 1
                    martix[i][maxLeft] = idx
                maxLeft += 1
            direction = (direction + 1) % 4

            if idx >= n ** 2:
                return martix


if __name__ == '__main__':
    n = 3
    print(Solution1().generateMatrix(n))