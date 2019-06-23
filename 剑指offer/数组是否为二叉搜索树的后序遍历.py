#!/usr/bin/env python
#coding:utf-8
#@author: rye
#@time: 2019/6/23 22:10

# -*- coding:utf-8 -*-
# https://www.cnblogs.com/yqpy/p/9748966.html
'''
思路解析：
    解题思路：
首先要清楚，这道题不是让你去【判断】一个给定的数组【是不是】一个（原先）给定的二叉搜索树的对应后序遍历的结果，【而是判断】一个给定的数组是不是能够对应到一个具体的二叉搜索树的后序遍历结果

所以还是用递归的思想。

把数组分成三部分，比如[4,8,6,12,16,14,10]，10就是根节点，4,8,6都是左子树，12,16,14,10都是右子树，然后针对左右子树再去判断是不是符合根节点、左右子树这一个规律（左子树都比根节点小，右子树都比根节点大）


'''
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if len(sequence) == 0:
            return False
        root = sequence[-1]
        index = 0
        for i in range(len(sequence)):
            if sequence[i] > root:
                index = i
                break
        for j in range(i, len(sequence) - 1):
            if sequence[j] < root:
                return False
        left = True
        right = True
        if len(sequence[:index]) > 0:
            left = self.VerifySquenceOfBST(sequence[:index])
        if len(sequence[index : -1]) > 0:
            right = self.VerifySquenceOfBST(sequence[index: -1])
        return left and right