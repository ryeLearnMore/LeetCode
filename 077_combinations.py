#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@author: rye
#@time: 2019/3/26

'''

因为知道是按tag刷的，所以知道用回溯法，但是这里本来就是我的弱项，还没有很好的把握方法，所以没做出来。
参考了https://github.com/apachecn/awesome-algorithm/blob/master/docs/Leetcode_Solutions/Python/0077._combinations.md
发现离正确方法差一点。

tips：
下面两个结构，作者貌似用了很多次，必须多加理解这种题。
check(tmp + [nums[idx]], idx + 1)
check(tmp, idx + 1)

'''

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        nums = [i for i in range(1, n + 1)]
        res = []

        def check(tmp, idx):
            if len(tmp) == k:
                res.append(tmp)
                return
            if idx < n:
                check(tmp + [nums[idx]], idx + 1)
                check(tmp, idx + 1)

        check([], 0)
        return res

# 大佬的代码
class Solution1:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        def dfs(cur_nums, idx):
            if len(cur_nums) == k:
                self.res.append(cur_nums)
                return
            if idx == n + 1:
                return
            dfs(cur_nums+[idx], idx+1)
            dfs(cur_nums, idx+1)
        self.res = []
        dfs([], 1)
        return self.res

if __name__ == '__main__':
    n = 4
    k = 2
    print(Solution().combine(n, k))