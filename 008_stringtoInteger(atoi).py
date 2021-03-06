#-*-coding:utf-8-*- 
__author__ = 'Rye'

class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        # strip()方法介绍
        # http://www.runoob.com/python/att-string-strip.html
        str = str.strip()
        if str == "":
            return 0

        if str[0] == '-':
            sign = -1
            str = str[1:]
        elif str [0] =='+':
            sign = 1
            str = str[1:]
        else:
            sign = 1

        sum = 0
        for i in str:
            if i >= '0' and i <= '9':
            	# ord()函数的应用
                # http://www.runoob.com/python/python-func-ord.html
                sum = ord(i) - ord('0') + sum * 10  # 字符串转化为数字方法
            else:
                break
        sum = sum * sign
        if sum < -2 ** 31:
            return -2 ** 31
        elif sum > 2 ** 31 - 1:
            return 2 ** 31 - 1
        else:
            return sum


if __name__ == '__main__':
    str1 = "12jghj"
    str2 = "-91283472332"
    str3 = '+123asdf'
    print(Solution().myAtoi(str3))
