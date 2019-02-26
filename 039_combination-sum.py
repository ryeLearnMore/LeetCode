#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@author: rye
#@time: 2019/2/26

# 不对。有一点思路，但是无法找到如【2，2，3】这种连续的结果。
'''
tips：
1. 多理解递归的适用条件。在这种情况下使用递归
2. 注意递归里参数的设定，多调试，多理解

'''
class Solution:
    def combinationSum(self, candidates: 'List[int]', target: 'int') -> 'List[List[int]]':
        candidates.sort(reverse=True)
        res = []

        target_ = target
        while candidates[-1] <= target:
            res_ = []
            while candidates[-1] <= target:
                for i in candidates:
                    if target >= i:
                        target -= i
                        res_.append(i)
                        break
            if target == 0:
                res.append(res_)

            target = target_
            candidates = candidates[1:]

        return res


# 按照思路自己重写一遍
class Solution2:
    def combinationSum(self, candidates: 'List[int]', target: 'int') -> 'List[List[int]]':
        def find(result, temp, index):
            if result == 0:
                res.append(temp)
                return
            for i in range(index, len(candidates)):
                if candidates[i] > result:
                    break
                find(result - candidates[i], temp + [candidates[i]], i)

        res = []
        candidates = list(set(candidates))
        candidates.sort()
        find(target, [], 0)
        return res

# 大佬的代码
class Solution1(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def dfs(remain, combo, index):
            if remain == 0:
                res.append(combo)
                return
            for i in range(index, len(candidates)):
                if candidates[i] > remain:
                    break
                dfs(remain - candidates[i], combo + [candidates[i]], i)
        candidates = list(set(candidates))
        candidates.sort()
        res = []
        dfs(target, [], 0)
        return res

if __name__ == '__main__':
    candidates = [2, 3, 6, 7]
    target = 7
    print(Solution1().combinationSum(candidates, target))