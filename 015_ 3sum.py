#!/usr/bin/env python
#coding:utf-8
#@author: rye
#@time: 2019/1/26 20:55

# 参考资料：https://github.com/ryeLearnMore/awesome-algorithm/blob/master/docs/Leetcode_Solutions/Python/015._3sum.md
# 我的代码，超时。时间复杂度O(n^3)
class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        resultLis = []
        sNums = sorted(nums)
        lNums = []
        rNums = []

        # while sNums != []:
        #     # for i, j in zip(range(len(sNums), 0, -1), range(3)):
        #     #     print(i, j)
        #     for i in range(len(sNums)):
        #         j = len(sNums) - i - 1
        #         if abs(sNums[i]) > abs(sNums[j]):
        #             while sNums[j] >= 0:

        if len(sNums) >= 3:
            if list(set(sNums)) == [0]: #防止出现多个[0,0,0,0]
                return [[0, 0, 0]]

            for i in sNums:
                if i < 0:
                    lNums.append(i)
                else:
                    rNums.append(i)

            if (lNums == [] and rNums != [0, 0, 0]) or rNums == []:
                return []

            for k in range(len(rNums)):
                for i in range(len(lNums)):
                    for j in range(i + 1, len(lNums)):
                        if lNums[i] + lNums[j] + rNums[k] == 0:
                            resultLis.append([lNums[i], lNums[j], rNums[k]])
                            break
            if len(rNums) >= 3 and rNums[0] == rNums[1] == rNums[2] == 0:
                resultLis.append([0, 0, 0])

            for k in range(len(lNums)):
                for i in range(len(rNums)):
                    for j in range(i + 1, len(rNums)):
                        if rNums[i] + rNums[j] + lNums[k] == 0:
                            resultLis.append([rNums[i], rNums[j], lNums[k]])
                            break

            resultList = []                          #创建一个新列表
            for i in resultLis:                    #循环list里的每一个元素
                if i not in resultList:            #判断元素是否存在新列表中，不存在则添加，存在则跳过，以此去重
                    resultList.append(i)
            return resultList
        else:
            return []

# 大佬的代码，跟我当初的构想类似，借助快排思想，但当时总是考虑这个方法会漏掉一些情况
class Solution1:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []

        for i in range(len(nums)):
            if i == 0 or nums[i] > nums[i - 1]:
                l = i + 1
                r = len(nums) - 1
                while l < r:
                    s = nums[i] + nums[l] + nums[r]
                    if s == 0:
                        res.append([nums[i], nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                        while r > l and nums[r] == nums[r + 1]:
                            r -= 1
                    elif s > 0:
                        r -= 1
                    else:
                        l += 1
        return res

if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    nums1 = [0, 0, 0]
    nums2 = [0]
    nums3 = [-1,0,1,0]
    nums4 = [-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]
    nums5 = [-4,-2,1,-5,-4,-4,4,-2,0,4,0,-2,3,1,-5,0]
    print(Solution1().threeSum(nums2))