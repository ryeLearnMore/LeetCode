#-*-coding:utf-8-*- 
__author__ = 'Rye'

class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = 0
        token = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
                 (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
        for n, t in token:
            length = len(t)
            while t == s[:length]:
                num += n
                s = s[length:] #此处不能用s.lstrip(t)。因为如果为'III'则查找到'I'时会把后面的两个'I'都删除掉

        return num

if __name__ == '__main__':
    s1 = 'MCMXCIV'
    s2 = 'LVIII'
    s3 = 'III'
    s4 = 'CC'
    print(Solution().romanToInt(s4))
