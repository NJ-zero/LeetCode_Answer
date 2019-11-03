# coding=utf-8
# Time: 2019-10-21-17:16 
# Author: dongshichao
'''
泰波那契序列 Tn 定义如下： 

T0 = 0, T1 = 1, T2 = 1, 且在 n >= 0 的条件下 Tn+3 = Tn + Tn+1 + Tn+2
给你整数 n，请返回第 n 个泰波那契数 Tn 的值。

示例 1：

输入：n = 4
输出：4
解释：
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4
示例 2：

输入：n = 25
输出：1389537

'''

class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1
        else:
            return self.tribonacci(n-1)+self.tribonacci(n-2)+self.tribonacci(n-3)

    def tribb(self, n):
        res= [0,1,1,2]
        if n <=3:
            return res[n]
        for i in range(3,n):
            res.append(res[-1]+res[-2]+res[-3])
        return res[-1]


s = Solution()
print(s.tribb(25))