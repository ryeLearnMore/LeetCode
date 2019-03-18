#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@author: rye
#@time: 2019/3/18

# lambda + sorted()的应用，注意理解匿名函数的应用
# https://www.cnblogs.com/hf8051/p/8085424.html
'''
tips:
1. 排序的理解，关于sorted(key = )的应用
2. 在for 或 while 等动态过程中，删除某一个list中的元素后，len(list)的值保持不变。
    所以，在实际应用中，为了保持某个指针的位置相对不变，需要借用变量count记录删除的
    值，在while的过程中用len的值减去count，并且，在相应的语句后面也要让i -= 1

'''
# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        sortedList = sorted(intervals, key=lambda x: x[0])
        i = 0
        list_len = len(sortedList) - 1
        count = 0
        while i < list_len - count:
            if sortedList[i][1] >= sortedList[i + 1][0]:
                if sortedList[i][1] > sortedList[i + 1][1]:
                    sortedList.remove(sortedList[i + 1])
                    count += 1
                    i -= 1
                else:
                    sortedList[i][1] = sortedList[i + 1][1]
                    sortedList.remove(sortedList[i + 1])
                    count += 1
                    i -= 1
            i += 1

        return sortedList


if __name__ == '__main__':
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    intervals1 = [[1,4],[0,2],[3,5]]
    print(Solution().merge(intervals1))