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
考研的时候复习过，不过现在忘了。。。回想ing
参考链接
https://github.com/apachecn/awesome-algorithm/blob/master/docs/Leetcode_Solutions/Python/0105._construct_binary_tree_from_preorder_and_inorder_traversal.md
总结：
一句话，看到树🌲就要想到递归！
'''
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if preorder == None:
            return None
        root = TreeNode(preorder[0])
        k = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:k + 1], inorder[0:k])
        root.right = self.buildTree(preorder[k + 1:], inorder[k + 1:])
        return root

# 这种思路也不错，从inorder入手，很好理解。
class Solution1(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if inorder:
            ind = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[ind])
            root.left = self.buildTree(preorder, inorder[0:ind])
            root.right = self.buildTree(preorder, inorder[ind+1:])
            return root

# 非递归，日后学习。现在时间是：2019.3.31
class Solution2(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder:
            return None
        stack=[]#利用栈后进先出的原理
        root=TreeNode(preorder[0])
        stack.append(root)
        index=0
        for i in range(1,len(preorder)):
            cur=stack[-1]
            if(stack[-1].val!=inorder[index]): #表明该中序索引在左子树
                cur.left=TreeNode(preorder[i])
                stack.append(cur.left)
            else:
                while(len(stack)!=0 and stack[-1].val==inorder[index]):
                    cur=stack.pop() #表明该子树一表达完毕
                    index+=1
                if(index<len(inorder)):
                    cur.right=TreeNode(preorder[i])
                    stack.append(cur.right)
        return root

if __name__ == '__main__':
    pass