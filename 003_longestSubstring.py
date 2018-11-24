#-*-coding:utf-8-*- 
__author__ = 'Rye'

# 子串和子序列区别
# http://www.voidcn.com/article/p-chadvurj-zu.html

# 我的代码。。。
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        res_list = []
        length = len(s)

        for i in range(length):
            tmp = s[i]
            for j in range(i + 1, length):
                if s[j] not in tmp:
                    tmp += s[j]
                else:
                    break
            res_list.append(tmp)

        maxSubString = 0
        for i in range(0, len(res_list)):
            if res_list[0]:
                if maxSubString < len(res_list[i]):
                    maxSubString = len(res_list[i])
            else:
                return 0
        return maxSubString

# 大佬的代码
class Solution1(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = 0
        max_len = 0
        d = {}

        # enumerate
        # http: // www.runoob.com / python3 / python3 - func - enumerate.html
        for i, c in enumerate(s):
            if c in d and d[c] >= start:
                max_len = max(max_len, i - start)
                start = d[c] + 1
            d[c] = i
        return max(max_len, len(s) - start)

if __name__ == '__main__':
    str1 = "abca"
    str2 = ""
    str3 = "bbbbb"
    str4 = "pwwkew"
    solution = Solution1().lengthOfLongestSubstring(str4)
    print(solution)
