# coding=utf-8
# Time: 2019-11-26-19:54 
# Author: dongshichao
'''
300. 最长上升子序列

给定一个无序的整数数组，找到其中最长上升子序列的长度。

示例:

输入: [10,9,2,5,3,7,101,18]
输出: 4
解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。


思路：
dp[i] 的值代表 nums 前 i 个数字的最长子序列长度

dp[i] = max(dp[i], dp[j] + 1) for j in [0, i)。

'''

class Solution:
    def lengthOfLIS(self, nums):
        if nums == []:
            return 0
        dp = [1] * len(nums)

        for i in range(1,len(nums)):
            for j in range(i):
                if (nums[j] < nums[i]):
                    dp[i] = max(dp[i],dp[j]+1)
        print(dp)
        return max(dp)

s=Solution()
print(s.lengthOfLIS([10,9,2,5,3,7,101,18,6]))

