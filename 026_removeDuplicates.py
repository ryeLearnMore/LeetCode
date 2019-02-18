#!/usr/bin/env python
#coding:utf-8
#@author: rye
#@time: 2019/2/18 17:15

'''
很快就写完了。。。算是最近写题最快的一个
'''
class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        j = 0
        while j < len(nums):
            if nums[j] == nums[i]:
                j += 1
            else:
                nums[i + 1] = nums[j]
                i += 1
                j += 1
        return len(nums[:i + 1])

if __name__ == '__main__':
    nums1 = [0,0,0,1,1,1,2,2,3,3,4]
    print(Solution().removeDuplicates(nums1))