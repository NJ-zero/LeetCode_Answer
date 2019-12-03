# coding=utf-8
# Time: 2019-11-07-17:15 
# Author: dongshichao

'''

507.完美数
对于一个 正整数，如果它和除了它自身以外的所有正因子之和相等，我们称它为“完美数”。
给定一个 整数 n， 如果他是完美数，返回 True，否则返回 False

 
示例：

输入: 28
输出: True
解释: 28 = 1 + 2 + 4 + 7 + 14

思路：
从2 到 num**0.5
如果能被num 整除，则 + i + num/i
得到结果和 num 相等

'''

class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <=1 :
            return False
        import math

        s=1
        for i in range(2,int(math.sqrt(num))+1):
            if num % i ==0:
                s += i + num/i

        return s ==num
