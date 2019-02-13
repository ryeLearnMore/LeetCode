#!/usr/bin/env python
#coding:utf-8
#@author: rye
#@time: 2019/2/12 17:29

# 我的代码，注意理解题意是关键！
'''
学到的知识点：
1. 理解题意
2. 学习字典中的取值方法
'''
class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        def find(str1, str2):
            ult = []
            for i in range(len(str1)):
                for j in range(len(str2)):
                    ult.append(str1[i] + str2[j])
            return ult

        dict = {'2': 'abc', '3' : 'def', '4' : 'ghi', '5' : 'jkl', '6' : 'mno', '7' : 'pqrs', '8': 'tuv', '9': 'wxyz'}
        res = []

        for i in range(len(digits)):
            # if i == digits[0]:
            if i == 0:
                length = len(dict[digits[0]])
                for j in range(length):
                    res.append(dict[digits[0]][j]) # 从字典中的两种取值方法。法1
            else:
                res = find(res, dict.get(digits[i])) # 从字典中的两种取值方法。法2

        return res

# 大佬的代码
'''
用哈希表,用递归查找，注意理解！多用debug调试

hash table一个，用来对应digit -> letter
s用来记录结果，每次从digits里面去一个，然后寻找其可能的char，加到s中，digits长度减小
digits长度为0时候，把它加入结果
'''

class Solution1(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        lookup = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        res = []

        def helper(s, digits):
            if len(digits) == 0:
                res.append(s)
            else:
                cur_digit = digits[0]
                for char in lookup[cur_digit]:
                    helper(s + char, digits[1:])

        if not digits or len(digits) == 0:
            return res
        helper('', digits)
        return res

if __name__ == '__main__':
    num1 = "23"
    num2 = "22"
    print(Solution1().letterCombinations(num1))