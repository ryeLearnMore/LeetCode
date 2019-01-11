# -*-coding:utf-8-*-
__author__ = 'Rye'

# 我的代码
class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        RomanString = ''
        while num > 0:
            if num // 1000:
                Mnum = num // 1000
                RomanString = RomanString + Mnum * 'M'
                num = num % 1000
                continue
            if num // 500:
                Dnum = num // 500
                RomanString += Dnum * 'D'
                num = num % 500
                continue
            if num // 100:
                if num // 100 == 4:
                    RomanString += 'CD'
                else:
                    Cnum = num // 100
                    RomanString += Cnum * 'C'
                num = num % 100
                continue
            if num // 50:
                Lnum = num // 50
                RomanString += Lnum * 'L'
                num = num % 50
                continue
            if num // 10:
                if num // 10 == 4:
                    RomanString += 'XL'
                else:
                    Xnum = num // 10
                    RomanString += Xnum * 'X'
                num = num % 10
                continue
            if num // 5:
                Vnum = num // 5
                RomanString += Vnum * 'V'
                num = num % 5
                continue
            else:
                if num == 4:
                    RomanString += 'IV'
                else:
                    RomanString += num * 'I'
                break
                # return RomanString

        if 'VIV' in RomanString:  # 9
            RomanString = RomanString.replace('VIV', 'IX')
        if 'LXL' in RomanString:  # 90
            RomanString = RomanString.replace('LXL', 'XC')
        if 'DCD' in RomanString:  # 900
            RomanString = RomanString.replace('DCD', 'CM')

            # if 'CCCC' in RomanString:  # 400
            #     RomanString = RomanString.replace('CCCC', 'CD')

            # if 'XXXX' in RomanString:  # 40
            #     RomanString = RomanString.replace('XXXX', 'XL')

            # if 'IIII' in RomanString:  # 4
            #     RomanString = RomanString.replace('IIII', 'IV')
        return RomanString


# 大佬的代码
class Solution1(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        lookup = {
            'M': 1000,
            'CM': 900,
            'D': 500,
            'CD': 400,
            'C': 100,
            'XC': 90,
            'L': 50,
            'XL': 40,
            'X': 10,
            'IX': 9,
            'V': 5,
            'IV': 4,
            'I': 1
        }
        roman = ''
        # sorted()
        # http://www.runoob.com/python3/python3-func-sorted.html
        '''
        sorted 的应用，也可以通过 key 的值来进行数组/字典的排序，比如：

        array = [{"age":20,"name":"a"},{"age":25,"name":"b"},{"age":10,"name":"c"}]
        array = sorted(array,key=lambda x:x["age"])
        print(array)
        输出结果：

        [{'age': 10, 'name': 'c'}, {'age': 20, 'name': 'a'}, {'age': 25, 'name': 'b'}]
        '''
        # key=lambda t: t[1]限制的是以字典‘：’右边的数字进行升序排序
        for symbol, val in sorted(lookup.items(), key=lambda t: t[1])[::-1]:
            while num >= val:
                roman += symbol
                num -= val
        return roman

# 大佬的代码
class Solution2:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        res = ''
        token = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
        for n, t in token:
            while num >= n:
                res += t
                num -= n
        return res

if __name__ == '__main__':
    num = 27
    num1 = 1994
    num2 = 4
    num3 = 9
    print(Solution1().intToRoman(num))