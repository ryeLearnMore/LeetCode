#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@author: rye
#@time: 2019/3/13
'''
总结：
思路正解差不多，但是过不了，原因在于如果strs里有重复的字符串就无法处理。
还没想好怎么解决。

'''
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        arr = []
        have = []

        for i in range(len(strs)):
            temp = []
            if strs[i] not in have:
                temp.append(strs[i])
            for j in range(i + 1, len(strs)):
                if sorted(strs[i]) == sorted(strs[j]):
                    if strs[j] not in have:
                        temp.append(strs[j])
                        have.append(strs[j])

            if temp != []:
                arr.append(temp)

        return arr

# 大佬的做法
'''
用字典的方式，感觉确实开拓了思路。
'''
class Solution1(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        mapx = {}
        for i in strs:
            tmp = ''.join(sorted(list(i)))
            if tmp in mapx:
                mapx[tmp].append(i) # 注意这步，自己写的时候可能想不到还可以这样添加。即：一个key对应多个value，并用list表示
            else:
                mapx[tmp] = [i]
        return mapx.values()

if __name__ == '__main__':
    strs1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
    strs2 = ["","",""]
    print(Solution1().groupAnagrams(strs1))