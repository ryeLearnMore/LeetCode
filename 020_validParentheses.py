#!/usr/bin/env python
#coding:utf-8
#@author: rye
#@time: 2019/2/15 11:04

'''
虽然是道简单题，但是因为目前还没用过栈，所以还没会，看了官方解题步骤https://leetcode-cn.com/problems/valid-parentheses/solution/
知道怎么做了
tips:
1. 学习该题的解题思路
2. 学习使用栈
3. 学习使用hashmap！
'''
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        # The stack to keep track of opening brackets.
        stack = []

        # Hash map for keeping track of mappings. This keeps the code very clean.
        # Also makes adding more types of parenthesis easier
        mapping = {")": "(", "}": "{", "]": "["}

        # For every bracket in the expression.
        for char in s:

            # If the character is an closing bracket
            if char in mapping:

                # Pop the topmost element from the stack, if it is non empty
                # Otherwise assign a dummy value of '#' to the top_element variable
                top_element = stack.pop() if stack else '#'

                # The mapping for the opening bracket in our hash and the top
                # element of the stack don't match, return False
                if mapping[char] != top_element:
                    return False
            else:
                # We have an opening bracket, simply push it onto the stack.
                stack.append(char)

        # In the end, if the stack is empty, then we have a valid expression.
        # The stack won't be empty for cases like ((()
        return not stack



if __name__ == '__main__':
    s1 = "()[]{}"
    s2 = "(]"
    s3 = '()'
    print(Solution().isValid(s3))