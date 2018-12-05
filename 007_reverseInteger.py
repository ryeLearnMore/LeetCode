#-*-coding:utf-8-*- 
__author__ = 'Rye'

# https://blog.csdn.net/coder_orz/article/details/52039990
class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            x = int(str(x)[::-1][-1] + str(x)[::-1][:-1])
        else:
            x = int(str(x)[::-1])
        x = 0 if abs(x) > 0x7FFFFFFF else x
        return x

class Solution1:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # if x >= 0:
        #     flag = 1
        # else:
        #     flag = -1
        flag = 1 if x >= 0 else -1
        abs_x = abs(x)
        answer = 0
        while abs_x > 0:
            answer = answer * 10 + abs_x % 10
            abs_x = abs_x // 10

        answer = flag * answer
        return answer if answer < 2147483648 and answer >= -2147483648 else 0

if __name__ == '__main__':
    print(Solution1().reverse(0))