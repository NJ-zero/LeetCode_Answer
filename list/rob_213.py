# coding=utf-8
# Time: 2019-12-28-11:19 
# Author: dongshichao

'''
213.打家劫舍II

问题同 198 ，区别在于 首尾是在一起的，不能同时打劫

问题转换为：
1。不偷窃 第一个房子
2。不偷窃 最后一个房子
取以上两种情况的max


'''
class Solution:
    def rob(self, nums):
        if not nums:
            return 0
        if len(nums) <=2:
            return max(nums)
        def helper(nums):
            if not nums:
                return 0
            if len(nums) <= 2:
                return max(nums)
            n = len(nums)
            dp = [0 for _ in range(n)]
            dp[0] = nums[0]
            dp[1] = max(nums[0],nums[1])
            for i in range(2,n):
                dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
            return dp[-1]

        return max(helper(nums[1:]),helper(nums[:-1]))

s= Solution()
print(s.rob([1,2,3,4]))
