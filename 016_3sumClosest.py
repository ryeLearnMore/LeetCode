#!/usr/bin/env python
#coding:utf-8
#@author: rye
#@time: 2019/2/10 10:33
'''
通过第15，16题，学会一种思想，即：如何在一个数组中找三个数，判单三个树的和的一些关系！
15，16题的具体区别就是具体问题具体分析

Python中可以用如下方式表示正负无穷：
float("inf"), float("-inf")，具体例子如class Solution()1中所示
'''
class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        nums.sort()

        for i in range(len(nums)):
            if i == 0 or nums[i] > nums[i - 1]:
                l = i + 1
                r = len(nums) - 1
                while l < r:
                    sums = nums[i] + nums[l] + nums[r]
                    if l == 1 and r == len(nums) - 1:
                        minNumber = abs(sums - target)
                        minSum = sums
                    if abs(sums - target) < minNumber:
                        minNumber = abs(sums - target)
                        minSum = sums
                        # r -= 1
                        # l += 1
                        # while l < r and nums[l] == nums[l - 1]:
                        #     l += 1
                        # while l < r and nums[r] == nums[r + 1]:
                        #     r -= 1
                    if sums > target:
                        r -= 1
                    if sums < target:
                        l += 1
                    if sums == target:
                        return minSum

        return minSum

# 大佬的代码
class Solution1(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n, res, diff = len(nums), None, float('inf')#正无穷
        nums.sort()
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, n-1
            while l < r:
                tmp = nums[i] + nums[l] + nums[r]
                if tmp == target:
                    return target
                elif tmp > target:
                    r -= 1
                    if abs(tmp-target) < diff:
                        diff = abs(tmp-target)
                        res = tmp
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
                else:
                    l += 1
                    if abs(tmp-target) < diff:
                        diff = abs(tmp-target)
                        res = tmp
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
        return res

if __name__ == '__main__':
    nums = [-1, 2, 1, -4]
    nums1 = [1,1,1,1]
    nums2 = [0,2,1,-3]
    nums3 = [0,0,0]
    nums4 = [1,1,-1,-1,3]
    nums5 = [1,2,4,8,16,32,64,128]

    print(Solution().threeSumClosest(nums5, 82))