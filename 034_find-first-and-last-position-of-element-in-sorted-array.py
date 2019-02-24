#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@author: rye
#@time: 2019/2/23

# 我的代码
'''
自己写的没通过，看了答案按照思想写的代码
tips：
1. 注意学习二分法在不同场景的运用
2. 注意二分法中，关于中间值nums[mid] 大于或小于 target后，后面一句跟的不同，两个if后跟的并不一样，如果一样会因相等时出错。
            if nums[med] < target:
         ---->  l = med + 1
            else:
                r = med - 1
    和
            if nums[med] > target: # 此处不能为if nums[med] < target: l = med + 1。对于target == nums[med]时会出错
         ---->  r = med - 1
            else:
                l = med + 1
'''
class Solution:
    def searchRange(self, nums: 'List[int]', target: 'int') -> 'List[int]':
        l = 0
        r = len(nums) - 1
        s = []

        # 先找左边界
        while l <= r:
            med = l + ((r - l) >> 1)

            if nums[med] == target and (med == 0 or nums[med - 1] != target):
                s.append(med)
                break

            if nums[med] < target:
                l = med + 1
            else:
                r = med - 1

        # 再找右边界
        r = len(nums) - 1
        while l <= r:
            med = l + ((r - l) >> 1)

            if nums[med] == target and (med == len(nums) - 1 or nums[med + 1] != target):
                s.append(med)
                break

            if nums[med] > target: # 此处不能为if nums[med] < target: l = med + 1。对于target == nums[med]时会出错
                r = med - 1
            else:
                l = med + 1

        if s != []:
            return s
        else:
            return [-1, -1]

# 大佬的代码
'''
二分法，先找target出现的左边界，判断是否有target后再判断右边界

找左边界：二分，找到一个index
该index对应的值为target
并且它左边index - 1
对应的值不是target（如果index为0则不需要判断此条件）
如果存在index就将其append到res中
判断此时res是否为空，如果为空，说明压根不存在target，返回[-1, -1]
找右边界：二分，找到一个index（但是此时用于二分循环的l可以保持不变，r重置为len(nums) - 1，这样程序可以更快一些）
该index对应的值为target
并且它右边index + 1
对应的值不是target（如果index为len(nums) - 1
则不需要判断此条件）
如果存在index就将其append到res中
AC
代码
'''

class Solution1(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums or len(nums) == 0:
            return [-1, -1]

        res = []
        l, r = 0, len(nums) - 1
        # search for left bound
        while l <= r:
            mid = l + ((r - l) >> 2)
            if nums[mid] == target and (mid == 0 or nums[mid - 1] != target):
                res.append(mid)
                break
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        if not res:
            return [-1, -1]

        # search for right bound
        r = len(nums) - 1
        while l <= r:
            mid = l + ((r - l) >> 2)
            if nums[mid] == target and (mid == len(nums) - 1 or nums[mid + 1] != target):
                res.append(mid)
                break
            if nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
                # 这里直接返回res是因为前面如果判断左边界没返回的话就说明我们判断右边界的时候一定会append元素
        return res

if __name__ == '__main__':
    nums = [5, 7, 7, 8, 8, 10]
    target = 8
    nums1 = [2, 2, 2, 2]
    target1 = 2
    print(Solution().searchRange(nums, target))