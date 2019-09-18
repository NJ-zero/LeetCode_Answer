# coding=utf-8
# Time: 2019-09-18-15:48 
# Author: dongshichao


'''
你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。

示例 1:

输入: [1,2,3,1]
输出: 4
解释: 偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
     偷窃到的最高金额 = 1 + 3 = 4 。
示例 2:

输入: [2,7,9,3,1]
输出: 12
解释: 偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
     偷窃到的最高金额 = 2 + 9 + 1 = 12 。

思路：
用递归

定义向量dp
dp向量长度与输入数组nums相同，dp[i]表示到第下标为i的房屋位置，可以打劫到的最大金额；

（1）当i=0时，打劫到第一家为止最大的打劫金额为这一家的金额，即dp[0]=nums[0]
（2）当i=1时，由于相邻房屋不能同时打劫，因此打劫到第二家位置的最大打劫金额为前两家中的最大值，即dp[1]=max(nums[0], nums[1])

i>2时：
（1）如果打劫下标为i的房间，这样下标为i-1的房间不能打劫，则当前的最大总金额为打劫到i-2房间的金额与下标为i的房间的金额之和；
（2）不打劫下标为i的房间，则当前的最大金额等于打劫到i-1房间的最大金额；
取两个选择的最大值，因此有：
dp[i] = max(dp[i-2] + nums[i], dp[i-1])

'''


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)

        else:
            s1 = self.rob(nums[:-1])
            s2 = self.rob(nums[-2])
            return max(s1,s2+nums[-1])

    def rob2(self,nums):
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        dp = [ 0 for _ in range(len(nums))]
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])
        for i in range(2,len(nums)):
            dp[i] = max(dp[i-2]+nums[i],dp[i-1])
        return dp[-1]

if __name__ == "__main__":
    s = Solution()
    print(s.rob2([2,1,1,2,3,3]))