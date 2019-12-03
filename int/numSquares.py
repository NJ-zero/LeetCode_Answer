# coding=utf-8
# Time: 2019-11-25-17:40 
# Author: dongshichao

'''
279.完全平方数

给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。

示例 1:
输入: n = 12
输出: 3
解释: 12 = 4 + 4 + 4.

示例 2:
输入: n = 13
输出: 2
解释: 13 = 4 + 9.

思路：
当前正整数n的结果对应于n去掉一个完全平方数之后的子问题结果加一
dp[i] = min(dp[i],dp[i-j*j]+1)

'''

class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [i for i in range(n+1)]
        print(dp)
        for i in range(1,n+1):
            j=1
            while i-j*j>=0:
                print(i,999,dp[i],dp[i-j*j])
                dp[i] = min(dp[i],dp[i-j*j]+1)
                print(i,dp[i])
                j+=1
        print(dp)
        return dp[n]


s=Solution()
print(s.numSquares(9))