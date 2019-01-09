#-*-coding:utf-8-*- 
__author__ = 'Rye'

class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
# 应用贪心算法
# https://github.com/apachecn/awesome-algorithm/blob/master/docs/Leetcode_Solutions/Python/011._container_with_most_water.md
        left = 0
        right = len(height) - 1
        maxArea = 0

        while left < right:
            if height[left] < height[right]:
                Area = height[left] * (right - left)
                if maxArea < Area:
                    maxArea = Area
                left += 1
            else:
                Area = height[right] * (right - left)
                if maxArea < Area:
                    maxArea = Area
                right -= 1
        return maxArea




# 超时
class Solution1:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        maxArea = 0
        length = len(height)
        smaller = 0
        for i in range(length):
            for j in range(i + 1, length):
                if height[i] <= height[j]:
                    smaller = height[i]
                else:
                    smaller = height[j]
                Area = smaller * (j - i)
                if maxArea < Area:
                    maxArea = Area

        return maxArea


if __name__ == '__main__':
    num = [1, 8, 6, 2, 5, 4, 8, 3, 7] # 输出: 49
    print(Solution().maxArea(num))

