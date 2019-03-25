#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@author: rye
#@time: 2019/3/25

'''
可能是由于对相对路径的认识不够，把问题复杂化了，开始考虑按照题目中的几条规则逐一处理，还考虑过用正则处理一下
但是看了答案之后发现，还是答案的方案好。以split‘/’进行分割，问题就简化了很多，然后按照规则处理。
tips:
1. strs.split('/')
2. '/'.join(path)
3. 栈的练习
'''
class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        # print(path.split("/"))
        for part in path.split("/"):
            if part and part != ".": # 如果为空或者 "." 则忽略
                if part == "..":
                    if stack:
                        stack.pop()
                else:
                    stack.append(part)
        if not stack:
            return "/"
        else:
            # join方法
            # http://www.runoob.com/python/att-string-join.html
            return "/" + "/".join(stack)

class Solution1(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        path = [i for i in path.split('/') if i]
        path2 = []
        for i in path:
            if i == '.':
                continue
            elif i == '..':
                if len(path2) > 0:
                    path2.pop(-1)
            else:
                path2.append(i)
        return '/' + '/'.join(path2)

# 自己按照思路1写的练习代码
class Solution3():
    def simplifyPath(self, path):

        stack = []
        for part in path.split('/'):
            if part != '.' and part:
                if part == '..':
                    if stack:
                        stack.pop()
                else:
                    stack.append(part)
        if stack:
            return '/' + '/'.join(stack)
        else:
            return '/'


if __name__ == '__main__':
    path = "/a/../../b/../c//.//"
    print(Solution3().simplifyPath(path))