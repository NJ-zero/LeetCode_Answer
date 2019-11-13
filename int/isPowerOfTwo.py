# coding=utf-8
# Time: 2019-11-13-19:22 
# Author: dongshichao
'''

给定一个整数，编写一个函数来判断它是否是 2 的幂次方。

示例 1:

输入: 1
输出: true
解释: 20 = 1
示例 2:

输入: 16
输出: true
解释: 24 = 16

'''

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n >0 and 2**31 % n ==0

    def isPpp(self,n):
        '''
        若 n= 2**X
        则说明，二进制最高位 1 其他位 都是 0
        n-1 最高位位 0 其他位 是 1
        二者 位与 & 运算结果一定位 0
        :param n:
        :return:
        '''
        return n >0 and n &(n-1) == 0