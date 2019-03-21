#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@author: rye
#@time: 2019/3/21

# 先暂时提交上去，后面一定要多看几遍。
'''
这道题是真的不会啊，看了答案感觉没有思路可循，有点难受。
参考链接：https://github.com/ryeLearnMore/awesome-algorithm/blob/master/docs/Leetcode_Solutions/Python/079._word_search.md

'''
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board:
            return False

        row = len(board)
        col = len(board[0]) if row else 0

        if row == 0:
            return False
        if row != 0 and col == 0:
            return False
        if not word or word == '':
            return True

        def dfs(i, j, idx):
            if i < 0 or j < 0 or i > row - 1 or j > col - 1 or board[i][j] != word[idx]:
                return False
            if idx == len(word) - 1:
                return True
            board[i][j] = '*'  # mark as visited
            res = dfs(i + 1, j, idx + 1) or dfs(i, j + 1, idx + 1) or dfs(i - 1, j, idx + 1) or dfs(i, j - 1, idx + 1)
            board[i][j] = word[idx]  # backtrack
            return res

        return any(dfs(i, j, 0) for i in range(row) for j in range(col))


if __name__ == '__main__':
    board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    word = "ABCCED"
    print(Solution().exist(board, word))