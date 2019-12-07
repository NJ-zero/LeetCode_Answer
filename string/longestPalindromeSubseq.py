# coding=utf-8
# Time: 2019-12-07-14:34 
# Author: dongshichao

'''

给定一个字符串s，找到其中最长的回文子序列。可以假设s的最大长度为1000。

示例 1:
输入:
"bbbab"
输出:
4
一个可能的最长回文子序列为 "bbbb"。


同 最长回文子串 不一样，回文子序列，可以不连续

dp[i][j]:以下标i为起始点，下标j为结束点的子串的最长回文子序列长度
每一个数都是一个会问子序列，所以 dp[i][i] = 1
状态可以转化位"
s[i]==s[j]: dp[i][j] = d[i+1]dp[j-1]+2
s[i]!=s[j]: dp[i][j] = max(dp[i+1,j],d[i,j-1])

[[0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0]]

因为 s[i]!=s[j] 会用到 dp[i+1][j] 的数据，所以i 要自下而上，j 自左而右

'''

class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp = [[0]*n for _ in range(n)]
        print(dp)
        for i in range(n):
            dp[i][i] = 1
        for i in range(n-1)[::-1]:
            for j in range(i+1,n):
                if s[i]==s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i][j-1],dp[i+1][j])
            print(dp)

        return dp[0][-1]

s= Solution()
print(s.longestPalindromeSubseq("bbbab"))