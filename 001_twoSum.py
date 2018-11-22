#-*-coding:utf-8-*- 
__author__ = 'Rye'


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
                    break

class Solution1(object):
    def twoSum(self, nums, target):
        for k, v in enumerate(nums):
            ret = target - nums[k]
            index = nums.index(ret)
            if ret in nums and index != k:
                return [k, index]

if __name__ == "__main__":
    s = Solution1()
    l = s.twoSum([3,2,4], 6)
    print(l)
#
# if __name__ == '__main__':
#     nums = [2, 7, 11, 15]
#     target = 6
#     x = Solution()
#     print(x.twoSum(nums, target))


