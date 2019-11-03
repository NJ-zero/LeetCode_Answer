# coding=utf-8
# Time: 2019-10-16-11:12 
# Author: dongshichao

'''
有两种特殊字符。第一种字符可以用一比特0来表示。第二种字符可以用两比特(10 或 11)来表示。

现给一个由若干比特组成的字符串。问最后一个字符是否必定为一个一比特字符。给定的字符串总是由0结束。
bits[i] 总是0 或者 1

示例 1:

输入:
bits = [1, 0, 0]
输出: True
解释:
唯一的编码方式是一个两比特字符和一个一比特字符。所以最后一个字符是一比特字符。
示例 2:

输入:
bits = [1, 1, 1, 0]
输出: False
解释:
唯一的编码方式是两比特字符和两比特字符。所以最后一个字符不是一比特字符。

解题思路：
遍历数组：当前 0 向前走 1 步，当前 1 向前走 2 步，最后能走到 len(bits) - 1


'''

class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        if bits[-1] == 1:
            return False
        pos = 0
        while pos < len(bits)-1:
            if bits[pos] == 0 :
                pos +=1
                print(0,pos)
            else:
                pos +=2
                print(1,pos)
        return pos == len(bits)-1

s=Solution()
print(s.isOneBitCharacter([1,0,1,1,0]))