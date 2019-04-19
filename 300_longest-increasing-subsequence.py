#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@author: rye
#@time: 2019/4/19

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1 or 0:
            return 1
        dp=[1 for i in range(len(nums))]
        maxresult=0
        for i in range(1,len(nums)):
            for j in range(0,i):
                if(nums[j]<nums[i]):
                    dp[i]=max(dp[i],dp[j]+1)
            maxresult=max(dp[i],maxresult)
        return maxresult


class Solution1(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n <= 1:
            return n
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[j] + 1, dp[i])
        return max(dp)


class AscentSequence:
    def findLongest(A, n):
        # write code here
        if n <= 1:
            return 0
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if A[i] > A[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

# 二分法
class Solution2(object):
    def binary_search(self,nums,num):
        start,end = 0,len(nums)-1
        while start<=end:
            mid = (start+end)//2
            if nums[mid]==num:
                return mid
            elif nums[mid]>num:
                end = mid-1
            else:
                start = mid+1
        return start
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        stack = nums[:1]
        for i in range(1,len(nums)):
            if nums[i]>stack[-1]:
                stack.append(nums[i])
            else:
                pos = self.binary_search(stack,nums[i])
                stack[pos] = nums[i]
        return len(stack)
if __name__ == '__main__':
    nums = [10,9,2,5,3,7,101]
    n = 7
    print(AscentSequence.findLongest(nums, 7))
    # print(Solution().lengthOfLIS(nums))