#!/usr/bin/env python
#coding:utf-8
#@author: rye
#@time: 2019/2/18 17:34

# 我的方法，没有通过。。。
'''
真的好蠢啊！明明知道应该跟上个题差不多，但是却给复杂化了，这样情况貌似发生过好几次了
做题之前应该理清思路，然后去做
PS：我的方法输出到【4，5】，val = 4时应该输出的是对的，但是提交显示的值和我运行的不一样！
目前没有发现原因
'''
class Solution1:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        nums.sort()

        i = 0
        j = 0
        while j < len(nums):
            if nums[j] == nums[i] and nums[j] != val:
                j += 1
            elif j == 0 and nums[j] == val:
                j += 1
                while j < len(nums) and nums[j] == nums[i]:
                    j += 1
                if j == len(nums):
                    return 0
                else:
                    return len(nums[j:])
            elif nums[j] != nums[i]:
                if nums[j] == val:
                    i = j - 1
                    while j < len(nums) and nums[j] == val:
                        j += 1
                    if j == len(nums):
                        return len(nums[:i + 1])
                    else:
                        nums[i + 1:] = nums[j:]
                        return len(nums)
                else:
                    i = j
                    j += 1
class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i, j =0, 0
        while j < len(nums):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
            j += 1
        return i

if __name__ == '__main__':
    nums = [0,0,1,2,2,3,0,4,2]
    val = 2
    nums1 = [3, 2, 2, 3]
    val1 = 3
    nums2 = [3, 3]
    val2 = 3
    nums3 = [4, 5]
    val3 = 4
    print(Solution().removeElement(nums3, val3))