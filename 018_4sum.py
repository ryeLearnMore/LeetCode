#!/usr/bin/env python
#coding:utf-8
#@author: rye
#@time: 2019/2/14 10:25

'''
我的代码，用了递归，本想尝试用O(n^2)解决，但是太天真，
虽然知道是固定两个数，然后用类似3sum去解决，但是我固定的是最前和最后的两个数。导致当有nums3那样
的列表时，总会因为判单l 或 r的值的大小（具体看代码，就理解我说的了）而漏解。很无奈，看了答案懂了
'''
class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def judge(tempI ,tempJ, flag):
            if nums[tempI] + nums[tempJ] > target and tempI < tempJ:
                return flag
            elif nums[tempI] + nums[tempJ] < target and tempI < tempJ:
                flag = 1
                return flag
            else:
                if tempI < tempJ:
                    judge(tempI + 1, tempJ - 1, flag)
                else:
                    flag = 2
                    return flag

        nums.sort()
        res = []

        if len(nums) < 4 or nums == []:
            return []

        i = 0
        j = len(nums) - 1

        while i < j:
            l = i + 1
            r = j - 1
            while l < r:
                sum_ = nums[i] + nums[j] + nums[l] + nums[r]
                if sum_ == target:
                    res.append([nums[i], nums[j], nums[l], nums[r]])
                    r -= 1
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                elif sum_ > target:
                    r -= 1
                else:
                    l += 1

            if nums[i] + nums[j] > target:
                j -= 1
            elif nums[i] + nums[j] < target:
                i += 1
            else:
                flag = 0
                tempI = i
                tempJ = j
                if judge(tempI + 1, tempJ - 1, flag) == 0 or 2:
                    j -= 1
                else:
                    i += 1

        return res

class Solution1(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        n = len(nums)
        nums.sort()
        res = []
        for i in range(n):
            for j in range(i+1,n):
                l, r = j+1, n-1
                while l < r:
                    temp = nums[i] + nums[j] + nums[l] + nums[r]
                    if temp == target:
                        if [nums[i],nums[j],nums[l],nums[r]] not in res:
                            res.append([nums[i],nums[j],nums[l],nums[r]])
                        l += 1
                        r -= 1
                    elif temp > target:
                        r -= 1
                    else:
                        l+=1
        return res

# 可以通过加判断条件，前后数字相等可以直接跳过，使得算法更快
class Solution2(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        n, res = len(nums), []
        nums.sort()
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:   # 因为i=0这个元素会直接往下执行
                continue
            for j in range(i+1, n):
                if j > i+1 and nums[j] == nums[j-1]:   # 因为j=i+1这个元素会直接往下执行
                    continue
                l, r = j+1, n-1
                while l < r:
                    tmp = nums[i] + nums[j] + nums[l] + nums[r]
                    if tmp == target:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                        while l < r and nums[r] == nums[r+1]:
                            r -= 1
                    elif tmp > target:
                        r -= 1
                    else:
                        l += 1
        return res
if __name__ == '__main__':
    nums1 = [1, 0, -1, 0, -2, 2]
    nums2 = [-3,-1,0,2,4,5]
    nums3 = [-3,-2,-1,0,0,1,2,3]

    target1 = 0
    target2 = 2
    print(Solution1().fourSum(nums3, target1))