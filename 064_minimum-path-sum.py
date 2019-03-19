#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@author: rye
#@time: 2019/3/19
'''
因为有62，63题做铺垫，所以这题一看就知道是dp，所以按照前两题的思想一下子就做出来了。
但是实现过程中有两处小问题，应该还是不熟练造成的，要多加联系。
'''
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # if not grid or len(grid) == 0:
        #     return 0
        # row = len(grid)
        # col = len(grid[0]) if row else 0
        row = len(grid)
        col = len(grid[0])

        dp = [[0 for i in range(col)] for j in range(row)]
        dp[0][0] = grid[0][0]
        # first row
        for i in range(1, col):
            dp[0][i] = grid[0][i] + dp[0][i - 1]

        # first col
        for j in range(1, row):
            dp[j][0] = grid[j][0] + dp[j - 1][0]

        for i in range(1, row):
            for j in range(1, col):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

        return dp[row - 1][col - 1]


if __name__ == '__main__':
    grid = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
    grid1 = [[1,2],[5,6],[1,1]]
    grid2 = [[1,2,5],[3,2,1]]
    print(Solution().minPathSum(grid2))