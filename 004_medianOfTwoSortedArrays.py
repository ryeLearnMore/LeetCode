#-*-coding:utf-8-*- 
__author__ = 'Rye'

'''
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
'''
# 正确写法，需要多次学习
# https://github.com/apachecn/awesome-algorithm/blob/master/docs/Leetcode_Solutions/Python/004._median_of_two_sorted_arrays.md
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        def findKth(A, B, k):
            if len(A) == 0:
                return B[k - 1]
            if len(B) == 0:
                return A[k - 1]
            if k == 1:
                return min(A[0], B[0])

            a = A[k // 2 - 1] if len(A) >= k // 2 else None
            b = B[k // 2 - 1] if len(B) >= k // 2 else None
            if b is None or (a is not None and a < b):
                return findKth(A[k // 2:], B, k - k // 2)
            return findKth(A, B[k // 2:], k - k // 2)

        num = len(nums1) + len(nums2)
        if num % 2 == 1:
            return self.findKth(nums1, nums2, num // 2 + 1)
        else:
            smaller = self.findKth(nums1, nums2, num // 2)
            larger = self.findKth(nums1, nums2, num // 2 + 1)
            return (smaller + larger) / 2.0

# 自己写的，侥幸也能通过，不过时间复杂度不对
class Solution1:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        num = sorted(nums1 + nums2)

        if len(num) % 2 == 1:
            result = (len(num) - 1) / 2
            # print(result)
            return num[int(result)]
        else:
            result1 = int(len(num) / 2)
            result2 = result1 - 1
            result = (num[int(result1)] + num[int(result2)]) / 2
            return result