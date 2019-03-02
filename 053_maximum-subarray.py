#!/usr/bin/env python
#coding:utf-8
#@author: rye
#@time: 2019/3/1 22:33
# 最后方法：动态规划
'''
看到是个简单题，于是用了双重循环做了，发现超时。。。
然后享用l = 0, r = len(nums) - 1的方法做，发现最后遇到 temp1 == temp2时总是出错
所以直接看答案。。。发现是动态规划
定位题目关键词：“连续”， “最大”
tips：
1.
'''
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #         max_ = nums[0]

        #         for i in range(len(nums)):
        #             for j in range(i, len(nums)):
        #                 if sum(nums[i : j + 1]) > max_:
        #                     max_ = sum(nums[i : j + 1])

        #         return max_
        l, r = 0, len(nums) - 1
        max_ = sum(nums)
        while l < r:
            temp1 = sum(nums[l + 1: r + 1])
            temp2 = sum(nums[l: r])
            if temp1 > temp2:
                if temp1 >= max_:
                    if l + 1 < len(nums):
                        max_ = sum(nums[l + 1: r + 1])
                l += 1
            elif temp2 > temp1:
                if temp2 >= max_:
                    if r > 0:
                        max_ = sum(nums[l: r])
                r -= 1
            else:
                if sum(nums[l + 2 : r + 1]) > temp2:
                    l += 1
                r -= 1

        return max_

# 大佬的代码
'''
maxSum[i-1] + nums[i] 记录的是前i个最大子序列的和。
要多理解，可以从len(nums) == 2时开始想，慢慢推，就理解了
参考链接：https://github.com/ryeLearnMore/awesome-algorithm/blob/master/docs/Leetcode_Solutions/Python/053._maximum_subarray.md
'''
class Solution1(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        maxSum = [nums[0] for i in range(n)]
        for i in range(1,n):
            maxSum[i] = max(maxSum[i-1] + nums[i], nums[i])
        return max(maxSum)

if __name__ == '__main__':
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    nums1 = [-2, -1]
    print(Solution1().maxSubArray(nums))