#!/usr/bin/env python
#coding:utf-8
#@author: rye
#@time: 2019/6/19 23:43

# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        # write code here
        i, j = 0, 0
        while i < len(array):
            if array[i] % 2 == 0:
                while j < len(array):
                    if array[j] % 2 == 1:
                        if j > i:
                            j += 1
                            continue
                        else:
                            array[i], array[j] = array[j], array[i]
                    else:
                        j += 1
            else:
                i += 1
        return array

if __name__ == '__main__':
    array = [2, 1, 3, 5, 6]
    print(Solution().reOrderArray(array))