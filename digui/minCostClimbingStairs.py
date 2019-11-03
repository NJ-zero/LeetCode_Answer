# coding=utf-8
# Time: 2019-10-16-14:23 
# Author: dongshichao

'''
数组的每个索引做为一个阶梯，第 i个阶梯对应着一个非负数的体力花费值 cost[i](索引从0开始)。

每当你爬上一个阶梯你都要花费对应的体力花费值，然后你可以选择继续爬一个阶梯或者爬两个阶梯。

您需要找到达到楼层顶部的最低花费。在开始时，你可以选择从索引为 0 或 1 的元素作为初始阶梯。

示例 1:

输入: cost = [10, 15, 20]
输出: 15
解释: 最低花费是从cost[1]开始，然后走两步即可到阶梯顶，一共花费15。
 示例 2:

输入: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
输出: 6
解释: 最低花费方式是从cost[0]开始，逐个经过那些1，跳过cost[3]，一共花费6。

思路：
状态：dp[i]表示到达第i个阶梯需要的最小花费；
dp[0] = cost[0]
dp[1] = cost[1]

状态转移方程：dp[i] = min( dp[i-2], dp[i-1] ) + cost[i];
'''

class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        dp = {}
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2,len(cost)):
            dp[i] = min(dp[i-1]+cost[i],dp[i-2]+cost[i])
            print(i,dp[i])
        return min(dp[len(cost)-1],dp[len(cost)-2])



s= Solution()
print(s.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))





