#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@author: rye
#@time: 2019/3/23

'''
查清了之间涉及到的数学关系，但是写代码还是没实现，最后参考了答案。具体解法及代码在下面class Solution1()上
参考链接：
https://github.com/ryeLearnMore/awesome-algorithm/blob/master/docs/Leetcode_Solutions/Python/060._permutation_sequence.md
'''
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        strs = ''
        length = n
        nums = [str(i) for i in range(1, n + 1)]
        k -= 1 # 少了这个。。。
        while len(strs) <= length:
            # if n == length:
            #     div = (n - 1) * (n - 2)
            #     xiabiao = (k // div)
            #     strs += nums[xiabiao]
            #     del nums[xiabiao]
            #     k = k % div
            #     n -= 1
            # if n > 2 and n < length:
            #     div = (n - 1) * (n - 2)
            #     xiabiao = (k // div) - 1
            #     strs += nums[xiabiao]
            #     del nums[xiabiao]
            #     k = k % div
            #     n -= 1
            if n > 2:
                div = (n - 1) * (n - 2) # 替换成n - 1的阶乘就可以
                xiabiao = (k // div)
                strs += nums[xiabiao]
                del nums[xiabiao]
                k = k % div
                n -= 1
            else:# 此时nums中应该只有两个元素了
                if k == 0:
                    strs += nums[0]
                    strs += nums[1]

                if k == 1:
                    strs += nums[1]
                    strs += nums[0]
                break
        return strs

# 大佬的代码：这题的思想是排列中涉及的数学关系，主要是k 与 n的阶乘之间的关系
'''
tips:
1.用动态规划的思想将N！N的阶乘保存在一个list中
2.用nums.pop()删除数组中的某个元素
3.k 一定要先减一！
'''

class Solution1(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        res = ''

        factorial = [1] * (n + 1)
        # factorial[] = [1, 1, 2, 6, 24, ... n!]
        for i in range(1, n + 1):
            factorial[i] = factorial[i - 1] * i

        # create a list of numbers to get indices
        nums = [i for i in range(1, n + 1)]
        # because we start from index 0
        k -= 1

        for i in range(1, n + 1):
            # this is the idx of first num each time we will get
            idx = k // factorial[n - i]
            res += str(nums[idx])
            # delete this num, since we have got it
            nums.pop(idx)
            # update k.这个步骤其实就是对k与n - i的阶乘取余，即之间涉及到的数学关系，以下两行代码都一个意思。
            # k -= idx * factorial[n - i]
            k = k % factorial[n - i]
        return res

if __name__ == '__main__':
    n = 4
    k = 2
    print(Solution1().getPermutation(n, k))