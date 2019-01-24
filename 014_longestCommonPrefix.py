class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        mixLength = 100000000
        Rstr = ''
        # 注意此处，每一步基本都要先判断是否为空和列表集合是否为空
        if strs == [] or strs == [""]:
            return ""
        # 学习如何求一个列表中，值的长度最小值。即：minl = min([len(x) for x in strs])
        for i in strs:
            if len(i) < mixLength:
                mixLength = len(i)
        for i in range(mixLength):
            for j in strs:
                temp = strs[0][i]
                if temp != j[i]:
                    return Rstr

            Rstr += temp

        if Rstr == '':
            return ""
        else:
            return Rstr

# 别人的
class Solution1:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]
        minl = min([len(x) for x in strs])
        end = 0
        while end < minl:
            for i in range(1, len(strs)):
                if strs[i][end] != strs[i - 1][end]:
                    return strs[0][:end]
            end += 1
        return strs[0][:end]



if __name__ == '__main__':
    strs1 = ["flower","flow","flight"]
    strs2 = ["dog","racecar","car"]
    strs3 = []
    strs4 = ["a"]
    strs5 = ["aca","cba"]
    print(Solution().longestCommonPrefix(strs4))