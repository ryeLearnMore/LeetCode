#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@author: rye
#@time: 2019/2/27

'''
理解了39题，这题自然就会做了。只需 i + 1
'''
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        def find(target, combo, index):
            if target == 0:
                if combo in res:
                    return
                else:
                    res.append(combo)
                    return # 不能用break
            for i in range(index, len(candidates)):
                if target >= candidates[i]:
                    find(target - candidates[i], combo + [candidates[i]], i + 1)
                else:
                    break

        # candidates = list(set(candidates))
        candidates.sort()
        res = []
        find(target, [], 0)
        return res

if __name__ == '__main__':
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    print(Solution().combinationSum2(candidates, target))