#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@author: rye
#@time: 2019/3/21

'''
两个代码都是自己写的。第一个不能过，第二个可以。
可能是受到上一题的影响，心态有点崩。后来看了一下26题的做法，按照上面的基础改了一下就做出来了。
'''

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return 1

        num = nums[0]
        i, num_count, tmp = 0, 1, 0
        while i < len(nums) - 1:
            if num_count <= 2 and nums[i + 1] == num:
                num_count += 1
                i += 1

            elif num_count > 2 and nums[i + 1] == num:
                tmp = i
                while nums[i + 1] == num:
                    i += 1
                swap_temp = i + 1 # 准备要换的值
                nums[tmp] = nums[swap_temp]

                i = swap_temp + 1
                num = nums[tmp]
                tmp += 1
                num_count = 1
            elif nums[i + 1] != num:
                num = nums[i + 1]
                num_count = 1
                i += 1

        return tmp, nums

class Solution1(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        j = 1
        cnt = 1
        while j < len(nums):
            if nums[j] == nums[i] and cnt < 2:
                nums[i + 1] = nums[j]
                j += 1
                i += 1
                cnt += 1
            elif nums[j] == nums[i] and cnt >= 2:
                j += 1
            else:
                cnt = 1
                nums[i + 1] = nums[j]
                i += 1
                j += 1

        return len(nums[:i + 1])
        # return nums[:i + 1]

if __name__ == '__main__':
    nums = [1, 1, 1, 2, 2, 3]
    nums1 = [0,0,1,1,1,1,2,3,3]
    print(Solution1().removeDuplicates(nums1))