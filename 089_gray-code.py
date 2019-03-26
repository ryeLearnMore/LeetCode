#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@author: rye
#@time: 2019/3/26

'''
这题如果自己想真的没看出规律。解法很多，下面这一个是我能看得懂的
https://blog.csdn.net/guoziqing506/article/details/51554879
解题思想：

这个题其实有个小技巧（个人一直觉得这种所谓的“技巧”其实并不能真正提高编程能力），就是编码的规律。什么规律呢？通过观察我们可以发现，格雷编码是通过上一级的编码得到的。也就是n个数的编码可以通过n  - 1个数的编码得到。
如果n = 1，那么编码为[0, 1]；
n = 2，编码为[00, 10, 11, 01]；
n = 3，编码为[000, 100, 110, 010, 011, 111, 101, 001]；
所以，n级的编码的生成，是从n - 1编码的最后一个编码开始倒序遍历，每遍历一个编码，就将这个编码+1后的码字添加到结果列表的后面，然后再将这个编码+0。
比如，n = 2，编码为[00, 10, 11, 01]，倒序遍历，得到：
01，+1后生成新的码字添加到后面，再对01+0，结果列表变成[00, 10, 11, 010, 011]；
接着向前遍历，对11做与上一步相同的处理，结果列表变成[00, 10, 110, 010, 011, 111]；
最后，结果列表变为[000, 100, 110, 010, 011, 111, 101, 001]。这样生成的编码就是符合格雷编码条件的。也就是说，n级格雷编码是由n - 1级格雷编码生成的，这是很典型的递归思想。
最后，把二进制的字符转换成十进制整数就行。代码如下：
---------------------
作者：guoziqing506
来源：CSDN
原文：https://blog.csdn.net/guoziqing506/article/details/51554879
版权声明：本文为博主原创文章，转载请附上博文链接！
'''

class Solution(object):
    def grayCode(self, n):
        result = []
        if n == 0:
            return [0]
        for i in self.helper(n):
            result.append(int(i, 2))
        return result

    def helper(self, n):
        result = []
        if n == 1:
            return ["0", "1"]
        elif n > 1:
            result = self.helper(n - 1)
            index = len(result) - 1
            while index >= 0:
                temp = result[index]
                temp += "1"
                result.append(temp)
                result[index] += "0"
                index -= 1
        return result

if __name__ == '__main__':
    n = 2
    print(Solution().grayCode(n))