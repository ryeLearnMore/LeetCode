#-*-coding:utf-8-*- 
__author__ = 'Rye'

'''
numRows = 4时
P     I    N       0    6      12         6  0
A   L S  I G  ---> 1  5 7   11 13   --->  4  2  这两列分别该行是从下往上需要走的步数和分别从上往下走的步数
Y A   H R          2 4  8 10              2  4  他们从两个方向走的步数都是固定的.如:二行一列的"A"到二行二列
P     I            3    9                 0  6  的"L",从下往上走加4,从"L"到"S"从下往上走加2,以此类推.
'''
class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        length = len(s)

        # 判断是否为空
        if s == '':
            return ''
        # 判断特殊情况：字符串长度小于行数和行数为1的情况
        if numRows == 1 or length <= numRows:
            return s
        # 后面是先画图，然后找规律想的，吧行数分别为3，4，5分别画出来，每个字母分别标出坐标就行

        else:
            step = 2 * (numRows - 1)
            finalString = ''
            for i in range(numRows):
                temp = s[i]
                count = i
                lineStep = step - i * 2
                if lineStep == step or lineStep == 0:
                    lineStep = step
                    count += lineStep

                    while count <= length - 1:
                        temp += s[count]
                        count += lineStep
                else:
                    while count <= length - 1:
                        count += lineStep
                        if count <= length - 1:
                            temp += s[count]
                            lineStep1 = step - lineStep
                            count += lineStep1
                            if count <= length - 1:
                                temp += s[count]

                finalString += temp
            return finalString


if __name__ == '__main__':
    s = "PAYPALISHIRING"
    s1 = 'AB'
    s2 = 'A'

    print(len(s))
    print(Solution().convert(s1, 1))



