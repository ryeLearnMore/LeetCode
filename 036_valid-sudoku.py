#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@author: rye
#@time: 2019/3/13
'''
tips:
1. 对于验证已有元素是否存在，要考虑使用哈希表的方法，通常最后一步都是验证key对应的value值是否 > 1
2. 字典的相关知识点：http://www.runoob.com/python/python-dictionary.html
'''
# 参考评论代码写的
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(9):
            row = []
            for j in range(9):
                if board[i][j] in row:
                    return False
                elif board[i][j] != '.':
                    row.append(board[i][j])

        for i in range(9):
            col = []
            for j in range(9):
                if board[j][i] in col:
                    return False
                elif board[j][i] != '.':
                    col.append(board[j][i])

        subs = [[] for i in range(9)]
        for i in range(9):
            for j in range(9):
                box_index = (i // 3) * 3 + j // 3 #关键！！！
                if board[i][j] != '.':
                    subs[box_index].append(board[i][j])

        for i in subs:
            if len(i) != len(set(i)):
                return False
        return True

# 标准解法
class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # init data
        rows = [{} for i in range(9)]
        columns = [{} for i in range(9)]
        boxes = [{} for i in range(9)]

        # validate a board
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != '.':
                    num = int(num)
                    box_index = (i // 3) * 3 + j // 3

                    # keep the current cell value
                    # 字典get方法：http://www.runoob.com/python/att-dictionary-get.html
                    rows[i][num] = rows[i].get(num, 0) + 1
                    columns[j][num] = columns[j].get(num, 0) + 1
                    boxes[box_index][num] = boxes[box_index].get(num, 0) + 1

                    # check if this value has been already seen before
                    if rows[i][num] > 1 or columns[j][num] > 1 or boxes[box_index][num] > 1:
                        return False
        return True

if __name__ == '__main__':
    board = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
    print(Solution().isValidSudoku(board))