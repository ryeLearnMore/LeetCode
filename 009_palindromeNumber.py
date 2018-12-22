#-*-coding:utf-8-*- 
__author__ = 'Rye'

# 与第007题很相似
class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        # 注意此处为什么要存储最初x的值！
        sourceX = x

        reverse = 0
        while x > 0:
            reverse = reverse * 10 + x % 10
            x = x // 10
        if reverse == sourceX or sourceX == 0:
            return True
        else:
            return False

class Solution1:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        return str(x) == str(x)[::-1]

if __name__ == '__main__':
    num1 = 121
    num2 = -121
    num3 = 10
    print(Solution().isPalindrome(num3))