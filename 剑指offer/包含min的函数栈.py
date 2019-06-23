#!/usr/bin/env python
#coding:utf-8
#@author: rye
#@time: 2019/6/23 18:04

'''
这题有点迷，没太懂出题的方向。。。
'''
# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack = []
        self.min_stack = []
    def push(self, node):
        # write code here
        self.stack.append(node)
        if not self.min_stack or node <= self.min_stack[-1]:
            self.min_stack.append(node)
    def pop(self):
        # write code here
        if self.stack[-1] == self.min_stack[-1]:
            self.min_stack.pop(-1)
        self.stack.pop(-1)
    def top(self):
        # write code here
        return self.statck.pop(-1)
    def min(self):
        # write code here
        return self.min_stack[-1]