#!/usr/bin/env python
#coding:utf-8
#@author: rye
#@time: 2019/5/1 11:02

class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here

        # row = len(array)
        # col = len(array[0])
        # for i in range(row):
        #     for j in range(col):
        #         if array[i][j] == target:
        #             return True
        # return False

        row = len(array)
        col = len(array[0])

        if row > 0 and col > 0:
            i = 0
            j = col - 1
            while i < row and j >= 0: # 注意此处是j >= 0，不是j > 0
                if array[i][j] == target:
                    return True
                elif array[i][j] > target:
                    j -= 1
                else:
                    i += 1
        return False

if __name__ =='__main__':
    target = 13
    array = [[1,2,3],[4,5,6],[7,8,9],[10,12,13]]
    answer = Solution()
    print(answer.Find(target,array))