#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@author: rye
#@time: 2019/3/31

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
'''
参考链接：
https://github.com/apachecn/awesome-algorithm/blob/master/docs/Leetcode_Solutions/Python/0111._minimum_depth_of_binary_tree.md
这道题有点坑，看了一眼评论，好像大部分都被【1， 2】这个测试用例倒下了

有一种特殊情况就是
注意leaf node: 反正就是没有left和right的
比如下图
1
 \
  2
2是一个孩子节点
这种情况应该输出2而不是1
唯一的特殊情况就是上面这种了，因为root下只有一个左节点或者是右节点，这样另外一边的空节点并不算是leaf node
'''
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        elif root.left and root.right:
            # return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
            return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
        elif root.left:
            return 1 + self.minDepth(root.left)
        elif root.right:
            return 1 + self.minDepth(root.right)
        else: # 这里是如果只有一个root节点，就返回1
            return 1


if __name__ == '__main__':
    pass 