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
# ---------------------------19.4.7-----------------------------
# 感觉下面这段代码更好，更容易理解
class Solution2(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lookup = {}
        for i, num in enumerate(nums):
            if target - num in lookup:
                return [lookup[target-num], i]
            else:
                # 向字典中添加新的键值对
                # 参考链接：http://www.runoob.com/python/python-dictionary.html
                lookup[num] = i
            
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


