#!/usr/bin/env python
#coding:utf-8
#@author: rye
#@time: 2019/2/16 9:32

'''
官方解题
因为这道题想了半天没有思路，当时考虑到可以用递归解决，但是想了半天没有思路，不知如何解决
直到看了标准答案，心中才知道大致要怎么处理
tips:
1. 正确理解递归工作原理
2. 多写多理解
'''
class Solution:
    def generateParenthesis(self, N):
        ans = []
        def backtrack(S = '', left = 0, right = 0):
            if len(S) == 2 * N:
                ans.append(S)
                return
            if left < N:
                backtrack(S+'(', left+1, right)
            if right < left:
                backtrack(S+')', left, right+1)

        backtrack()
        return ans
# class Solution1:
#     def generateParenthesis(self, n):
#         """
#         :type n: int
#         :rtype: List[str]
#         """
#         mapping = {'(':')'}
#         res = []
#         s = ''
#         stack = []
#
#         for i in range(n):
#             stack.append('(')
#
#         for i in range(n):
#             s += stack.pop()
#             if len(s) != n * 2:

if __name__ == '__main__':
    n = 3
    print(Solution().generateParenthesis(n))