#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@author: rye
#@time: 2019/3/25

'''
2019.3.25心得：
1. 原谅我只能看懂这个暴力回溯法，现在太渣，其他的方法感觉现在才疏学浅，实在看不懂。所以第一轮先放过这题吧。。。
2. 一般只要看到所有的组合，一般都是用回溯。
---------------时间分割线---------------------------
'''

class Solution(object):
    def restoreIpAddresses(self, s):
        if len(s)<4 or len(s)>12:
            return []
        lis=[]
        # m是段，以'.'分割。
        def bakctrack(tmp,n,m):
            if m>3:
                lis.append(tmp[:-1])
                return
            for i in range(1,4):
                if s[n]=="0" and i>1:
                    continue
                if int(s[n:n+i])<256 and len(s[n+i:])>=3-m and len(s[n+i:])<=3*(3-m):
                    bakctrack(tmp+s[n:n+i]+".",n+i,m+1)
                    if n+i>=len(s):
                        break
        bakctrack("",0,0)
        return lis


# https://blog.csdn.net/fuxuemingzhu/article/details/80657420
class Solution1(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        self.dfs(s, [], res)
        return res

    def dfs(self, s, path, res):
        if len(s) > (4 - len(path)) * 3:
            return
        if not s and len(path) == 4:
            res.append('.'.join(path))
            return
        for i in range(min(3, len(s))):
            curr = s[:i + 1]
            if (curr[0] == '0' and len(curr) >= 2) or int(curr) > 255:
                continue
            self.dfs(s[i + 1:], path + [s[:i + 1]], res)

'''
原谅我只能看懂这个暴力回溯法，现在太渣，其他的方法感觉现在才疏学浅，实在看不懂。所以第一轮先放过这题吧。。。
'''
class Solution2(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def dfs(s, sub, ips, ip):
            if sub == 4:
                if s == "":
                    ips.append(ip[1:])
                return
            for i in range(1,4):
                if i <= len(s):
                    if int(s[:i]) <= 255:
                        dfs(s[i:], sub + 1, ips, ip+"."+s[:i])
                    if s[0] == "0":
                        break
        ips = []
        dfs(s, 0, ips, "")
        return ips

if __name__ == '__main__':
    s = "25525511135"
    print(Solution2().restoreIpAddresses(s))