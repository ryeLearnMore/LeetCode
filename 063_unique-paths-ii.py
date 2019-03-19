#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@author: rye
#@time: 2019/3/19

# 33/43的时候卡了
'''
原本想要用62题的思路，借用一维数组来计算，但是实际发现很多测试用例都无法通过，所以感觉算法思想欠缺了点什么。
所以放弃看了答案。
tip:
学会遇到什么提醒，用什么样的方法。
'''
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if m < 1 or n < 1 or obstacleGrid[0][0] == 1:
            return 0
        dp = [0] * n

        for i in range(m):
            if obstacleGrid[i][0] == 0:
                dp[0] = 1
            else:
                dp[0] = 0
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    dp[j] += dp[j - 1]
                else:
                    dp[j] = 0
            if sum(dp) == 0: #
                return 0
        return dp[n - 1]

class Solution1(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """

        row = len(obstacleGrid)
        col = len(obstacleGrid[0])

        dp = [[0 for i in range(col)] for j in range(row)]

        dp[0][0] = int(obstacleGrid[0][0] == 0)

        # first row
        for i in range(1, col):
            if obstacleGrid[0][i] == 1:
                dp[0][i] = 0
            else:
                dp[0][i] = dp[0][i - 1]

        # first col
        for i in range(1, row):
            if obstacleGrid[i][0] == 1:
                dp[i][0] = 0
            else:
                dp[i][0] = dp[i - 1][0]

        for i in range(1, row):
            for j in range(1, col):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[row - 1][col - 1]

if __name__ == '__main__':
    obstacleGrid = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    obstacleGrid1 = [[1]]
    obstacleGrid2 = [[0], [1]]
    obstacleGrid3 = [[0,0],[1,1],[0,0]]
    obstacleGrid4 = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[1,0],[0,0],[0,0],[0,0],[0,0],[0,0],[1,0],[0,0],[0,0],[0,0],[0,0],[0,1],[0,0],[0,0],[1,0],[0,0],[0,0],[0,1],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,1],[0,0],[0,0],[0,0],[0,0],[1,0],[0,0],[0,0],[0,0],[0,0]]
    obstacleGrid5 = [[0,0,0],[0,1,0],[0,0,0]]
    print(Solution1().uniquePathsWithObstacles(obstacleGrid5))