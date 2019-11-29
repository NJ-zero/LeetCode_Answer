# coding=utf-8
# Time: 2019-11-28-19:55 
# Author: dongshichao
'''
416. 分割等和子集

给定一个只包含正整数的非空数组。是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。
注意:
每个数组中的元素不会超过 100
数组的大小不会超过 200

示例 1:
输入: [1, 5, 11, 5]
输出: true
解释: 数组可以分割成 [1, 5, 5] 和 [11].

思路：
dp[i][j]：表示从数组的 [0, i] 这个子区间内挑选一些正整数，每个数只能用一次，使得这些数的和等于 j
新来一个数，例如是 nums[i]，根据这个数可能选择也可能不被选择：

如果不选择 nums[i]，在 [0, i - 1] 这个子区间内已经有一部分元素，使得它们的和为 j ，那么 dp[i-1][j] = true；
如果选择 nums[i]，在 [0, i - 1] 这个子区间内就得找到一部分元素，使得它们的和为 j - nums[i] ，前提条件是 nums[i] <= j
dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i]], (nums[i] <= j)

'''

class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        s = sum(nums)
        if s % 2 != 0:
            return False
        target = s // 2
        dp = [[False for _ in range(target+1)] for _ in range(n)]

        for j in range(target+1):
            dp[0][j] = False if nums[0] != j else True

        for i in range(1,n):
            for j in range(target+1):
                if j >=nums[i]:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i]]
                else:
                    dp[i][j] = dp[i-1][j]
        print(dp)
        return dp[-1][-1]

s=Solution()
print(s.canPartition([1,5,11,2,3]))