#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@author: rye
#@time: 2019/3/30

'''
递归与迭代的关系
1） 递归中一定有迭代,但是迭代中不一定有递归,大部分可以相互转换。
2） 能用迭代的不用递归,递归调用函数,浪费空间,并且递归太深容易造成堆栈的溢出.
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# 未通过，因为跳过了100题，直接做的101题，想的是如果中序遍历是个回文的，那结果一定是对的。结果卡在了倒数第二个测试用例上：[5,4,1,null,1,null,4,2,null,2,null]
# 确实怎么都过不去，所以直接放弃，因为可能是想法错了。看了答案，
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        res = []

        def check(root, res):
            if root and root.left == None and root.right == None:
                res.append(root.val)
                return
            elif root == None:
                res.append('*')
                return
            else:
                check(root.left, res)
                res.append(root.val)
                check(root.right, res)
        check(root, res)
        print(res)
        l, r = 0, len(res) - 1
        while l <= r:
            if res[l] != res[r]:
                return False
            l += 1
            r -= 1

        return True

class Solution1(object):
    def judge(self, p, q):
        if p == None and q == None:
            return True
        if p and q and p.val == q.val: # 如果一边有一边没有那么直接返回False
            return self.judge(p.left, q.right) and self.judge(p.right, q.left)
        return False

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root:
            return self.judge(root.left, root.right)
        return True
# ---------------------
# 作者：Rude3knife
# 来源：CSDN
# 原文：https://blog.csdn.net/qqxx6661/article/details/75332482
# 版权声明：本文为博主原创文章，转载请附上博文链接！


if __name__ == '__main__':
    pass