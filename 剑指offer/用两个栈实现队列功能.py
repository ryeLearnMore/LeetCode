#!/usr/bin/env python
#coding:utf-8
#@author: rye
#@time: 2019/6/13 23:07

# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    def push(self, node):
        # write code here
        self.stack1.append(node)
        self.stack1.push()
    def pop(self):
        # return xx
        if len(self.stack2) == 0:
            while self.stack1:
                tmp = self.stack1.pop()
                self.stack2.append(tmp)
        return self.stack2.pop()
