# coding=utf-8 
# @Time    : 2020/4/2 7:46 下午
# @Author  : 'Shichao-Dong'

'''
191 位 1 的个数
编写一个函数，输入是一个无符号整数，返回其二进制表达式中数字位数为 ‘1’ 的个数（也被称为汉明重量）。

'''

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        while n > 0 :
            if n & 1 == 1:  # # 和1 位与 运算，两个都为 1，结果为 1
                res +=1
            n = n >> 1
        return res